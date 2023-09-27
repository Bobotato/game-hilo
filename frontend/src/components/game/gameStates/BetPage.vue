<script lang="ts" setup>
import { ref, Ref } from 'vue'

import PokerCard from '@/components/game/gameElements/PokerCard.vue';
import ErrorWarning from '@/components/errorWarning/ErrorWarning.vue';

import { BetPredictionError } from '@/errors/gameErrors'
import { RoundInfo } from '@/types/gameElements/gameElementTypes';
import { CardRanks, CardSuits } from '@/models/pokerCard';
import { Prediction } from '@/models/betPrediction'

interface Props {
    roundInfo: RoundInfo
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'submitBetPrediction', bet: number, prediction: Prediction): void
    (e: 'playAudio', sound: string): void
}>()

let bet: Ref<number> = ref(0)

let prediction: Ref<Prediction> = ref(Prediction.None)

let errorString: Ref<string> = ref("")

function selectPredictionButton(choice: Prediction) {
    emit('playAudio', 'choiceSelectSfx')
    prediction.value = choice
}

function submitBetPrediction() {
    try {
        validateBetPrediction()
        emit('playAudio', 'menuSelectSfx')
        emit('submitBetPrediction', bet.value, prediction.value)
    } catch (error) {
        console.error(error)
        emit('playAudio', 'errorBuzzer')
    }
}

function validateBetPrediction() {
    if (prediction.value === Prediction.None && bet.value === 0) {
        errorString.value = "You have not made any bet or prediction."
        throw new BetPredictionError("BetPredictionNotSelectedError")

    } else if (bet.value > props.roundInfo.player.credits) {
        errorString.value = "You cannot bet more than you have."
        throw new BetPredictionError("BetExceedsCreditsError")

    } else if (bet.value === 0) {
        errorString.value = "You cannot bet nothing."
        throw new BetPredictionError("NilBetError")

    } else if (prediction.value === Prediction.None) {
        errorString.value = "You have not chosen a prediction."
        throw new BetPredictionError("NilPredictionError")
    }
}
</script>

<template>
    <div class="bet-prediction-main">
        <div class="bet-prediction-menu">

            <h2 class="bet-prediction_current-card-message">
                Your current card is the {{ CardRanks[props.roundInfo.current_card.rank] }} of
                {{ CardSuits[props.roundInfo.current_card.suit] }}.
            </h2>

            <div class="bet-prediction_current-card">
                <PokerCard :card=props.roundInfo.current_card :isStatic="true"></PokerCard>
            </div>

            <div class="bet-prediction-message">
                Choose if the next card will be higher or lower, <br> and how much you're willing to bet.
            </div>

            <div class="bet-prediction-prediction-selection-wrapper">
                <button 
                    @click="selectPredictionButton(Prediction.Higher)"
                    :class="{ 'prediction-button prediction-button_higher': prediction == Prediction.None,
                              'prediction-button prediction-button_higher prediction-button_selected': prediction == Prediction.Higher,
                              'prediction-button prediction-button_higher prediction-button_unselected': prediction == Prediction.Lower }">
                    Higher
                </button>

                <button 
                    @click="selectPredictionButton(Prediction.Lower)"
                    :class="{ 'prediction-button prediction-button_lower': prediction == Prediction.None,
                              'prediction-button prediction-button_higher prediction-button_selected': prediction == Prediction.Lower,
                              'prediction-button prediction-button_higher prediction-button_unselected': prediction == Prediction.Higher }">
                    Lower
                </button>
            </div>

            <h2 class="bet-prediction_current-credits-message">
                You have {{ props.roundInfo.player.credits }} "credits".
            </h2>

            <input class="bet-prediction_bet-input"
                type="number" 
                min=0 
                :max=props.roundInfo.player.credits 
                v-model="bet" 
                required />

            <ErrorWarning class="error-warning" 
                v-if="errorString !== ''" 
                :errorString="errorString">
            </ErrorWarning>

            <button class="bet-prediction_submit-bet-prediction-button" 
                @click="submitBetPrediction">
                Confirm
            </button>
        </div>
    </div>
</template>

<style scoped>
.bet-prediction-main {
    display: grid;
    width: 100vw;
    height: 100vh;
    place-items: center;
}

.bet-prediction-menu {
    display: grid;
    grid-template-rows: [current-card-message] auto [current-card] 400px [bet-prediction-message] auto [prediction-buttons] auto [bet-label] auto [bet] auto [error-dialogue] auto [bet-prediction_submit-bet-prediction-button] auto;
    place-items: center;
}

.bet-prediction_current-card-message {
    grid-row: current-card-message;
    white-space: pre-wrap;
    text-align: center;
    font-size: 1.5em;
    color: white;
    line-height: 1.5em;
    margin: 0 0 20px 0;
}

.bet-prediction_current-card {
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

.bet-prediction-prediction-selection-wrapper {
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
    background-color: rgba(48, 0, 0);
}

.prediction-button_selected {
    background-color: rgb(90, 0, 0);
}

.prediction-button_unselected {
    color: grey;
    background-color: rgba(38, 38, 38);
}

.bet-prediction_bet-input {
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
    background: rgba(3, 3, 3);
}

.bet-prediction_bet-input::placeholder {
    color: white;
}

.bet-prediction_bet-input:focus {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    cursor: text;
}

.bet-prediction_bet-input:not(:focus):not(:placeholder-shown):invalid {
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

.bet-prediction_submit-bet-prediction-button {
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
    background-color: rgba(0, 48, 0);
}
</style>