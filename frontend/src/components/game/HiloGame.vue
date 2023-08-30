<script lang="ts" setup>
import { ref, Ref, onMounted } from 'vue'

import CardInventory from '@/components/game/gameElements/CardInventory.vue'
import DrawDeck from '@/components/game/gameElements/DrawDeck.vue'
import GetBetPrediction from '@/components/game/gameElements/GetBetPrediction.vue';
import StartMessage from '@/components/game/gameElements/StartMessage.vue';
import GameResult from '@/components/game/gameElements/GameResult.vue';
import WelcomeScreen from '@/components/game/gameElements/WelcomeScreen.vue'

import { Deck } from '@/classes/Deck'
import { Prediction } from '@/composables/gameElements/getBetPrediction';
import { Token } from '@/services/apiService/game/game';

import { useRoundInfoComposable, useRoundResultComposable } from '@/composables/hiloGame'
import { BetPredictionError } from '@/errors/gameErrors';
import { UnauthorisedError } from '@/services/apiService/errors';
import { RoundInfo } from '@/types/gameElements/gameElementTypes';

let { roundInfo, updateRoundInfo } = useRoundInfoComposable()
let { roundResult, updateRoundResult } = useRoundResultComposable()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

const token = { access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2OTM0MjYwNTB9.20vEIEmiRYhahCBtbV19OuKgk3k87eg6DLNV8urlu1k" }
enum GameStates {
    "start",
    "welcome",
    "deck",
    "betPrediction",
    "result"
}

let errorMessage = ref({
    message: "",
    isShowing: false
})

let isShowing = ref(GameStates.start)

let betPredictionStatus = ref({
    bet: 0,
    prediction: Prediction.None,
    isShowing: false
})

async function handleGetRoundInfo(token: Token) {
    try {
        await updateRoundInfo(token)
    } catch (error: any) {
        console.log(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorMessage.value.message = 'There is an issue with the login token. Please login again.'
                console.log(error.message)
                break
        }
    }
}

onMounted(() => {
    handleGetRoundInfo(token)
})

async function startRound(token: Token) {
    try {
        isShowing.value = GameStates.welcome
        await handleGetRoundInfo(token)
    } catch (error) {
        console.log(error)
    }
}
// function drawCard(deck: Deck) {
//     let drawnCard = deck.dealCard()
//     console.log(drawnCard)
//     if (drawnCard) {
//         gameDetails.value.currentCard = drawnCard
//         console.log(`Drew ${drawnCard}`)
//     }
//     isShowing.value = GameStates.betPrediction
// }

// function compareCards(drawnCard: Card, currentCard: Card) {
//     if (CardRanks.indexOf(drawnCard.rank) < CardRanks.indexOf(currentCard.rank)) {
//         return true
//     } else if (CardRanks.indexOf(drawnCard.rank) > CardRanks.indexOf(currentCard.rank)) {
//         return false
//     } else if (drawnCard.rank === currentCard.rank) {
//         if (CardSuits.indexOf(drawnCard.suit) < CardSuits.indexOf(currentCard.suit)) {
//             return true
//         } else if (CardSuits.indexOf(drawnCard.suit) > CardSuits.indexOf(currentCard.suit)) {
//             return false
//         }
//     }
// }

// function computeRoundResult(prediction: Prediction, currentCard: Card) {
//     console.log("Computing result")
//     let drawnCard = gameDetails.value.deck.dealCard()
//     console.log(drawnCard)
//     if (drawnCard instanceof Card) {
//         let result = compareCards(currentCard, drawnCard)
//         if (prediction === Prediction.Higher) {
//             return result
//         } else {
//             return !result
//         }
//     }
// }

function submitBetPrediction(bet: number, prediction: Prediction) {
    betPredictionStatus.value.bet = bet
    console.log(`Player bet ${betPredictionStatus.value.bet}`)
    betPredictionStatus.value.prediction = prediction
    console.log(`Player predicted ${Prediction[betPredictionStatus.value.bet]}`)
    isShowing.value = GameStates.result
    // console.log(computeRoundResult(prediction, gameDetails.value.currentCard))
}
</script>

<template>
    <div class=game>
        <StartMessage class=start-message-component v-if="isShowing === GameStates.start"
            @play-audio="$emit('playAudio', $event)" @change-active-game-state="startRound(token)">
        </StartMessage>

        <WelcomeScreen class="welcome-screen-component" v-if="isShowing === GameStates.welcome" :name=roundInfo.player.name
            :credits=roundInfo.player.credits>
        </WelcomeScreen>

        <DrawDeck class=draw-deck-component v-else-if="isShowing === GameStates.deck" :currentCard=roundInfo.current_card
            @play-audio="$emit('playAudio', $event)">
        </DrawDeck>

        <GetBetPrediction v-else-if="isShowing === GameStates.betPrediction" @submit-bet-prediction="submitBetPrediction"
            @play-audio=" $emit('playAudio', $event)" :currentCard=roundInfo.current_card
            :currentCredits=roundInfo.player.credits>
        </GetBetPrediction>

        <GameResult v-else-if="isShowing === GameStates.result" :drawnCard=roundResult.drawn_card :isWin=roundResult.win>
        </GameResult>
    </div>

    <h2 class="gamestate">Gamestate: {{ GameStates[isShowing] }}</h2>
    <!-- <h2 class="inventory-credits">Remaining "Credits": {{ roundInfo.player.credits }}</h2> -->

    <!-- <CardInventory v-if=false class="inventory-cards" :card=roundInfo.current_card>
        </CardInventory> -->
</template>

<style scoped>
.game {
    display: grid;
    width: 100vw;
    height: 100vh;
    place-items: center;
}

.gamestate {
    position: absolute;
    left: 10px;
    bottom: 0px;
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