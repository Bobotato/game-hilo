<script lang="ts" setup>
import { ref } from 'vue'

import CardInventory from '@/components/game/gameElements/CardInventory.vue'
import DrawDeck from '@/components/game/gameElements/DrawDeck.vue'
import GetBetPrediction from '@/components/game/gameElements/GetBetPrediction.vue';
import StartMessage from '@/components/game/gameElements/StartMessage.vue';

import { Card, CardRanks, CardSuits } from '@/classes/PokerCard';
import { Deck } from '@/classes/Deck'
import { Prediction } from '@/composables/gameElements/getBetPrediction';


const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let currentCard = ref(new Card(CardSuits[0], CardRanks[0]))

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

let drawDeck = ref({
    deck: new Deck(false, false),
    isShowing: false
})

function toggleBetPredictionMenu() {
    betPredictionStatus.value.isShowing = !betPredictionStatus.value.isShowing
}

function toggleDrawDeck() {
    drawDeck.value.isShowing = !drawDeck.value.isShowing
}


function updateBet(bet: number) {
    betPredictionStatus.value.bet = bet
}

function updatePrediction(prediction: Prediction) {
    betPredictionStatus.value.bet = prediction
}

function startNewGame() {
    let deck = new Deck(true, true)
    drawDeck.value.deck = deck
    console.log(deck.toString())
    console.log("Started game")
    toggleDrawDeck()
}

function drawCard(deck: Deck) {
    let drawnCard = deck.dealCard()
    toggleDrawDeck()
    console.log(drawnCard)
    if (drawnCard) {
        currentCard.value = drawnCard
        console.log(currentCard.value)
    }
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
        <StartMessage @start-game="startNewGame()" @play-audio="$emit('playAudio', $event)"></StartMessage>

        <DrawDeck v-if=drawDeck.isShowing @play-audio="$emit('playAudio', $event)" @draw-card="drawCard(drawDeck.deck)">
        </DrawDeck>

        <GetBetPrediction v-if=betPredictionStatus.isShowing @submit-bet-prediction="toggleBetPredictionMenu"
            @play-audio=" $emit('playAudio', $event)" :currentCard=currentCard :currentCredits=currentCredits>
        </GetBetPrediction>

        <h2 class="inventory-credits">Remaining "Credits": {{ currentCredits }}</h2>

        <CardInventory v-if=false class="inventory-cards" :card=currentCard>
        </CardInventory>
    </div>
</template>

<style scoped>
.game {
    display: grid;
    width: 100vw;
    height: 100vh;
    grid-template-rows: [game-events] auto [game-misc] auto;
    grid-template-columns: [left] 1fr [middle] 1fr [right] 1fr;
}

.bg-filter {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    backdrop-filter: blur(5px);
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