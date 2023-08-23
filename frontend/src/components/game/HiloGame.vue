<script lang="ts" setup>
import { ref, Ref } from 'vue'

import CardInventory from '@/components/game/gameElements/CardInventory.vue'
import DrawDeck from '@/components/game/gameElements/DrawDeck.vue'
import GetBetPrediction from '@/components/game/gameElements/GetBetPrediction.vue';
import StartMessage from '@/components/game/gameElements/StartMessage.vue';
import GameResult from '@/components/game/gameElements/GameResult.vue';

import { Card, CardRanks, CardSuits } from '@/classes/PokerCard';
import { Deck } from '@/classes/Deck'
import { Prediction } from '@/composables/gameElements/getBetPrediction';


const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

interface GameDetails {
    currentCredits: number
    currentCard: Card
    drawnCard: Card
    deck: Deck
}

let gameDetails: Ref<GameDetails> = ref({
    currentCredits: 10,
    currentCard: new Card(CardSuits[0], CardRanks[0]),
    drawnCard: new Card(CardSuits[0], CardRanks[0]),
    deck: new Deck(false, false),
})

enum GameStates {
    "welcome",
    "deck",
    "betPrediction",
    "result"
}

let isShowing = ref(GameStates.welcome)

let betPredictionStatus = ref({
    bet: 0,
    prediction: Prediction.None,
    isShowing: false
})

function startNewGame() {
    let deck = new Deck(true, true)
    gameDetails.value.deck = deck
    console.log(deck.toString())
    console.log("Started game")
    startRound(deck)
}

function startRound(deck: Deck) {
    isShowing.value = GameStates.deck
}

function drawCard(deck: Deck) {
    let drawnCard = deck.dealCard()
    console.log(drawnCard)
    if (drawnCard) {
        gameDetails.value.currentCard = drawnCard
        console.log(`Drew ${drawnCard}`)
    }
    isShowing.value = GameStates.betPrediction
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

function computeRoundResult(prediction: Prediction, currentCard: Card) {
    console.log("Computing result")
    let drawnCard = gameDetails.value.deck.dealCard()
    console.log(drawnCard)
    if (drawnCard instanceof Card) {
        let result = compareCards(currentCard, drawnCard)
        if (prediction === Prediction.Higher) {
            return result
        } else {
            return !result
        }
    }
}

function submitBetPrediction(bet: number, prediction: Prediction) {
    betPredictionStatus.value.bet = bet
    console.log(`Player bet ${betPredictionStatus.value.bet}`)
    gameDetails.value.currentCredits -= bet
    betPredictionStatus.value.prediction = prediction
    console.log(`Player predicted ${Prediction[betPredictionStatus.value.bet]}`)
    isShowing.value = GameStates.result
    console.log(computeRoundResult(prediction, gameDetails.value.currentCard))
}

function awardBet(bet: number) {
    gameDetails.value.currentCredits += bet
}
</script>

<template>
    <StartMessage class=start-message-component v-if="isShowing === GameStates.welcome" @start-game="startNewGame()"
        @play-audio="$emit('playAudio', $event)">
    </StartMessage>

    <DrawDeck class=draw-deck-component v-else-if="isShowing === GameStates.deck" @play-audio="$emit('playAudio', $event)"
        @drawCard="drawCard(gameDetails.deck)">
    </DrawDeck>

    <GetBetPrediction v-else-if="isShowing === GameStates.betPrediction" @submit-bet-prediction="submitBetPrediction"
        @play-audio=" $emit('playAudio', $event)" :currentCard=gameDetails.currentCard
        :currentCredits=gameDetails.currentCredits>
    </GetBetPrediction>

    <GameResult v-else-if="isShowing === GameStates.result" :drawnCard=gameDetails.drawnCard :isWin=true></GameResult>



    <div class=game v-if=false>

        <h2 class="inventory-credits">Remaining "Credits": {{ gameDetails.currentCredits }}</h2>

        <CardInventory v-if=false class="inventory-cards" :card=gameDetails.currentCard>
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