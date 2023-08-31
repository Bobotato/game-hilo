<script lang="ts" setup>
import { ref, Ref } from 'vue'

import PokerCard from '@/components/game/gameElements/PokerCard.vue';

import errorDialogue from '@/components/errorDialogue/errorDialogue.vue';

import { BetPredictionError } from '@/errors/gameErrors'
import { Card } from '@/types/gameElements/gameElementTypes';
import { CardRanks, CardSuits } from '@/services/card';

import { Prediction } from '@/composables/gameElements/getBetPrediction';

interface Props {
    currentCard: Card
    currentCredits: number
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'submitBetPrediction', bet: number, prediction: Prediction): void
    (e: 'playAudio', sound: string): void
}>()

let bet: Ref<number> = ref(0)

let prediction: Ref<Prediction> = ref(Prediction.None)

let errorHeader: Ref<string> = ref("")

let currentInventoryMessage: string = `Your current card is the ${CardRanks[props.currentCard.rank]} of ${CardSuits[props.currentCard.suit]}.\n You have ${props.currentCredits} "credits".`

let betPredictionMessage: string = `Choose if the next card will be higher or lower, \n and how much you're willing to bet.`

function selectPredictionButton(choice: Prediction) {
    emit('playAudio', 'choiceSelectSfx')
    prediction.value = choice
    console.log(prediction.value)
}

function checkBetandPrediction() {
    if (prediction.value === Prediction.None && bet.value === 0) {
        errorHeader.value = "You have not made any bet or prediction."
        throw new BetPredictionError("BetPredictionNotSelectedError")

    } else if (bet.value > props.currentCredits) {
        errorHeader.value = "You cannot bet more than you have."
        throw new BetPredictionError("BetExceedsCreditsError")

    } else if (bet.value === 0) {
        errorHeader.value = "You cannot bet nothing."
        throw new BetPredictionError("NilBetError")

    } else if (prediction.value === Prediction.None) {
        errorHeader.value = "You have not chosen a prediction."
        throw new BetPredictionError("NilPredictionError")
    }
}

function submitBetPrediction() {
    try {
        checkBetandPrediction()
        emit('playAudio', 'menuSelectSfx')
        emit('submitBetPrediction', bet.value, prediction.value)
    } catch (error) {
        console.log(error)
        emit('playAudio', 'errorBuzzer')
    }
}
</script>

<template>
    <div class="menu-wrapper">
        <div class="bet-prediction-menu">

            <div class="current-card-message">
                {{ currentInventoryMessage }}
            </div>

            <div class="current-card">
                <PokerCard :card=props.currentCard :isStatic="true"></PokerCard>
            </div>

            <div class="bet-prediction-message">
                {{ betPredictionMessage }}
            </div>

            <div class="prediction-button-wrapper">
                <button @click="selectPredictionButton(Prediction.Higher)"
                    :class="{ 'prediction-button higher': prediction == Prediction.None, 'prediction-button higher selected-button': prediction == Prediction.Higher, 'prediction-button higher unselected-button': prediction == Prediction.Lower }">
                    Higher
                </button>
                <button @click="selectPredictionButton(Prediction.Lower)"
                    :class="{ 'prediction-button lower': prediction == Prediction.None, 'prediction-button higher selected-button': prediction == Prediction.Lower, 'prediction-button higher unselected-button': prediction == Prediction.Higher }">
                    Lower
                </button>
            </div>

            <input class="bet-input" type="number" min=0 :max=props.currentCredits v-model="bet" required />

            <errorDialogue class="error-dialogue" v-if="errorHeader !== ''" :errorMessage="errorHeader">
            </errorDialogue>

            <button class="button submit-button" @click="submitBetPrediction">
                Confirm
            </button>
        </div>
    </div>
</template>

<style scoped>
.menu-wrapper {
    display: grid;
    width: 100vw;
    height: 100vh;
    place-items: center;
}

.bet-prediction-menu {
    display: grid;
    grid-template-rows: [current-card-message] auto [current-card] auto [bet-prediction-message] auto [prediction-buttons] auto [bet-label] auto [bet] auto [error-dialogue] auto [submit-button] auto;
    place-items: center;
}

.current-card-message {
    grid-row: current-card-message;
    white-space: pre-wrap;
    text-align: center;
    font-size: 1.5em;
    color: white;
    line-height: 1.5em;
    margin: 0 0 20px 0;
}

.current-card {
    width: 300px;
    height: 400px;
    scale: 90%;
    grid-row: current-card;
    margin: 0 0 20px 0;
}

.bet-prediction-message {
    grid-row: bet-prediction-message;
    white-space: pre-wrap;
    text-align: center;
    font-size: 1.5em;
    color: white;
    line-height: 1.5em;
    margin: 0 0 50px 0;
}

.prediction-button-wrapper {
    grid-row: prediction-buttons;
    display: flex;
    justify-content: center;
    gap: 50px;
    margin: 0 0 50px 0;
}

.prediction-button {
    height: 50px;
    width: 250px;
    border: none;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
    background-color: rgba(48, 0, 0, 80%);
}

.selected-button {
    background-color: rgb(90, 0, 0);
}

.unselected-button {
    color: grey;
    background-color: rgba(38, 38, 38, 0.8);
}

.bet-input {
    height: 50px;
    width: 80%;
    border: none;
    outline: none;
    font-size: 1.5em;
    color: white;
    text-align: left;
    font-weight: 300;
    margin: 0 0 25px 0;
    padding: 0px 0px 0px 20px;
    background: rgba(3, 3, 3, 70%);
}

.bet-input::placeholder {
    color: white;
}

.bet-input:focus {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    cursor: text;
}

.bet-input:not(:focus):not(:placeholder-shown):invalid {
    border: 1px solid rgb(151, 0, 0);
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

input[type=number] {
    -moz-appearance: textfield;
}

.submit-button {
    height: 50px;
    width: 250px;
    border: none;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
    margin: 25px 0 0 0;
    background-color: rgba(0, 48, 0, 80%);
}
</style>