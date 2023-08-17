<script lang="ts" setup>
import { ref, Ref } from 'vue'

import errorDialogue from '@/components/errorDialogue/errorDialogue.vue';

interface Props {
    currentCard: string
    currentCredits: number
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'setBet', bet: number): void
    (e: 'setPrediction', prediction: string): void
    (e: 'playAudio', sound: string): void
}>()

let bet: Ref<number> = ref(0)
let prediction: Ref<string> = ref("")

let errorHeader: Ref<string> = ref("")

let betPredictionMessage: string = `Your current card is ${props.currentCard}. \n\n Choose if the next card will be higher or lower, \n and how much you're willing to bet.`

function submitBetPrediction() {
    emit('playAudio', 'menuSelectSfx')
    emit('setBet', bet.value)
    emit('setPrediction', prediction.value)
}
</script>

<template>
    <div class="menu-wrapper">
        <div class="bet-prediction-menu">
            <div class="bet-prediction-message">
                {{ betPredictionMessage }}
            </div>

            <input autofocus type="text" class="input username-input" placeholder="Prediction" required>

            <input type="text" class="input bet-input" placeholder="Bet" required />

            <errorDialogue class="error_dialogue" v-if="errorHeader !== ''" :errorMessage="errorHeader">
            </errorDialogue>

            <button class="button submit-button" @click="submitBetPrediction">
                Confirm
            </button>
        </div>
    </div>
</template>

<style>
.menu-wrapper {
    display: grid;
    width: 100vw;
    height: 100vh;
    place-items: center;
}

.bet-prediction-menu {
    display: grid;
    grid-template-rows: [message] auto [prediction-label] auto [prediction] auto [bet-label] auto [bet] auto [submit-button] auto;
    place-items: center;
}

.bet-prediction-message {
    grid-row: message;
    white-space: pre-wrap;
    text-align: center;
    font-size: 1.5em;
    color: white;
    line-height: 1.5em;
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
    background-color: rgba(48, 0, 0, 80%);
}
</style>