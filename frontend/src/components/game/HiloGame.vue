<script lang="ts" setup>
import { ref } from 'vue'

import CardInventory from '@/components/game/gameElements/CardInventory.vue'
import ReceiveItem from '@/components/game/gameElements/ReceiveItem.vue'
import GetBetPrediction from './gameElements/GetBetPrediction.vue';

import { Card, CardRanks, CardSuits } from '@/classes/PokerCard';
import { Deck } from '@/classes/Deck'
import { Prediction } from '@/composables/gameElements/getBetPrediction';


const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let currentCard = ref()

let currentCredits = ref(10)

let betPredictionStatus = ref({
    bet: 0,
    prediction: "",
    isShowing: false
})

const newPlayerMessage = ref({
    message: "Welcome to the game. \n Let's get you started.",
    isShowing: true
})

let gameMessage = ref({
    message: `Welcome back to the game. \n You have ${currentCredits.value} "credits".`,
    isShowing: true
})

let receiveItemMenu = ref({
    isShowing: true
})

function toggleGameMessage() {
    gameMessage.value.isShowing = !gameMessage.value.isShowing
    emit('playAudio', 'menuSelectSfx')
}

function toggleReceiveItemMenu() {
    receiveItemMenu.value.isShowing = !receiveItemMenu.value.isShowing
    emit('playAudio', 'menuSelectSfx')
}

function toggleBetPredictionMenu() {
    betPredictionStatus.value.isShowing = !betPredictionStatus.value.isShowing
}

function updateBet(bet: number) {
    betPredictionStatus.value.bet = bet
}

function updatePrediction(prediction: Prediction) {
    betPredictionStatus.value.bet = prediction
}

function startGame() {
    toggleGameMessage()
    let deck = new Deck(true, true)
    console.log(deck.toString())

    if (currentCard.value == null) {
        currentCard.value = deck.dealCard()
    }
    console.log("Started game")
}

function compareCards(drawnCard: Card, currentCard: Card) {
    if (CardRanks.indexOf(drawnCard.rank) < CardRanks.indexOf(currentCard.rank)) {
        return true
    } else if (CardRanks.indexOf(drawnCard.rank) > CardRanks.indexOf(currentCard.rank)) {
        return false
    } else if (drawnCard.rank === currentCard.rank) {
        if (CardSuits.indexOf(drawnCard.suit) < CardSuits.indexOf(currentCard.suit)) {
            return true
        } else if (CardSuits.indexOf(drawnCard.suit) > CardSuits.indexOf(currentCard.suit)) {
            return false
        }
    }
}

function isWin(drawnCard: Card, prediction: Prediction) {
    console.log("win")
    return true
}

function computeRoundResult(bet: number, prediction: Prediction) {
    console.log("take bet")
    console.log("Computing result")
    isWin()
}


</script>

<template>
    <div class="game">
        <div v-if=gameMessage.isShowing class="game-message-card">
            <h2 class="game-message">{{ gameMessage.message }}</h2>
            <button class="game-message-button" @click=startGame()>Start Game</button>
        </div>

        <GetBetPrediction v-if=betPredictionStatus.isShowing @submit-bet-prediction="toggleBetPredictionMenu"
            @play-audio=" $emit('playAudio', $event)" :currentCard=currentCard :currentCredits=currentCredits>
        </GetBetPrediction>

        <h2 class="inventory-credits">Remaining "Credits": {{ currentCredits }}</h2>

        <CardInventory v-if=!gameMessage.isShowing class="inventory-cards" :card=currentCard></CardInventory>
    </div>
</template>

<style>
.game {
    display: grid;
    width: 100vw;
    height: 100vh;
    grid-template-rows: [game-events] auto [game-misc] auto;
    grid-template-columns: [left] 1fr [middle] 1fr [right] 1fr;
}

.game-message-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 30vh;
    grid-row: game-events;
    grid-column: middle;
}

.game-message {
    white-space: pre-wrap;
    line-height: 2em;
    text-align: center;
}

.game-message-button {
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


.game-events {
    grid-row: game-events;
    grid-column: middle;
    background: rgba(255, 0, 0, 0.235);
}

.inventory-credits {
    grid-row: game-misc;
    grid-column: left;
    align-self: end;
    padding: 0 0 5vh 5vw;
}

.inventory-cards {
    grid-row: game-misc;
    grid-column: middle;
    justify-self: center;
    align-self: end;
    margin: 0 0 5vh 0;
}
</style>