<script lang="ts" setup>
import { ref, Ref } from 'vue'

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

interface GameDetails {
    currentCredits: number
    currentCard: Card
    deck: Deck
}

let gameDetails: Ref<GameDetails> = ref({
    currentCredits: 10,
    currentCard: new Card(CardSuits[0], CardRanks[0]),
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
    prediction: "",
    isShowing: false
})

// function changeCurrentlyShowingComponent(component: string) {
//     if (isShowing != component) {
//         gameDetails.value.isShowing = component
//     } else {
//         gameDetails.value.isShowing = component
//     }
// }

// function updateBet(bet: number) {
//     betPredictionStatus.value.bet = bet
// }

// function updatePrediction(prediction: Prediction) {
//     betPredictionStatus.value.bet = prediction
// }

function startNewGame() {
    let deck = new Deck(true, true)
    gameDetails.value.deck = deck
    console.log(deck.toString())
    console.log("Started game")
    startRound(deck)
}

function startRound(deck: Deck) {
    drawCard(deck)
}

function drawCard(deck: Deck) {
    isShowing.value = GameStates.deck
    // let drawnCard = deck.dealCard()
    // console.log(drawnCard)
    // if (drawnCard) {
    //     gameDetails.value.currentCard = drawnCard
    //     console.log(`Drew ${drawnCard}`)
    // }
}

function takeBetPrediction() {
    isShowing.value = "betPrediction"
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
    <StartMessage class=start-message-component v-if="isShowing === GameStates.welcome" @start-game="startNewGame()"
        @play-audio="$emit('playAudio', $event)">
    </StartMessage>

    <DrawDeck class=draw-deck-component v-else-if="isShowing === GameStates.deck" @play-audio="$emit('playAudio', $event)"
        @drawCard="drawCard(gameDetails.deck)">
    </DrawDeck>

    <GetBetPrediction v-else-if="isShowing === GameStates.betPrediction" @submit-bet-prediction="toggleBetPredictionMenu"
        @play-audio=" $emit('playAudio', $event)" :currentCard=gameDetails.currentCard
        :currentCredits=gameDetails.currentCredits>
    </GetBetPrediction>



    <div class=game v-if="gameDetails.isShowing === 'game'">

        <h2 class="inventory-credits">Remaining "Credits": {{ gameDetails.currentCredits }}</h2>

        <CardInventory v-if=true class="inventory-cards" :card=gameDetails.currentCard>
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