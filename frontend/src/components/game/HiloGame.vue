<script lang="ts" setup>
import { ref, onMounted } from 'vue'

import WelcomePage from '@/components/game/gameStages/WelcomePage.vue'

import DrawDeck from '@/components/game/gameElements/DrawDeck.vue'
import GetBetPrediction from '@/components/game/gameElements/GetBetPrediction.vue';
import GameResult from '@/components/game/gameElements/GameResult.vue';

import GameOver from '@/components/game/gameElements/GameOver.vue';
import ErrorOverlay from '@/components/game/errorOverlay.vue';
import LoadingPage from '@/components/loading/LoadingPage.vue';

import { Prediction } from '@/composables/gameElements/getBetPrediction';

import { useRoundInfoComposable, useRoundResultComposable, GameStates } from '@/composables/hiloGame'
import { UnauthorisedError } from '@/services/apiService/errors';
import { AxiosError } from 'axios';

let { roundInfo, updateRoundInfo } = useRoundInfoComposable()
let { roundResult, updateRoundResult } = useRoundResultComposable()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let errorOverlay = ref({
    error: "",
    isShowing: false
})

let activeGameState = ref(GameStates.loading)

async function handleGetRoundInfo() {
    try {
        await updateRoundInfo()
    } catch (error: any) {
        console.log(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.error = 'There is an issue with the login token. Please login again.'
                errorOverlay.value.isShowing = true
                console.log(error.message)
                break
            case AxiosError:
                errorOverlay.value.error = 'There is an issue with the API server. Please try again later.'
                errorOverlay.value.isShowing = true
                console.log(error.message)
                break
        }
    }
}

async function handleGetRoundResult(bet: Bet, prediction: Prediction) {
    try {
        await updateRoundResult(bet, prediction)
    } catch (error: any) {
        console.log(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.error = 'There is an issue with the login token. Please login again.'
                errorOverlay.value.isShowing = true
                console.log(error.message)
                break
            case AxiosError:
                errorOverlay.value.error = 'There is an issue with the API server. Please try again later.'
                errorOverlay.value.isShowing = true
                console.log(error.message)
                break
        }
    }
}

async function startRound() {
    try {
        await handleGetRoundInfo()
        changeActiveGameState(GameStates.welcome)
    } catch (error) {
        console.log(error)
    }
}

async function submitBetPrediction(bet: number, prediction: number) {
    console.log(`Player bet ${bet}`)
    console.log(`Player predicted ${Prediction[prediction]}`)
    await handleGetRoundResult(bet, prediction)
    activeGameState.value = GameStates.result
}

async function endRound() {
    try {
        activeGameState.value = GameStates.betPrediction
        await handleGetRoundInfo()
    } catch (error) {
        console.log(error)
    }
}

function changeActiveGameState(gamestate: GameStates) {
    activeGameState.value = gamestate
}

startRound()
</script>

<template>
    <div class=game>
        <ErrorOverlay v-if="errorOverlay.isShowing" :error=errorOverlay.error @play-audio="$emit('playAudio', $event)">
        </ErrorOverlay>

        <loadingCover v-if="activeGameState === GameStates.loading"></loadingCover>

        <WelcomePage v-if="activeGameState === GameStates.welcome" :roundInfo=roundInfo
            @change-active-game-state="changeActiveGameState($event)" @play-audio="$emit('playAudio', $event)">
        </WelcomePage>

        <DrawDeck v-if="activeGameState === GameStates.deck" :currentCard=roundInfo.current_card
            @play-audio="$emit('playAudio', $event)" @change-active-game-state="activeGameState = GameStates.betPrediction">
        </DrawDeck>

        <GetBetPrediction v-else-if="activeGameState === GameStates.betPrediction" :roundInfo=roundInfo
            @submit-bet-prediction="submitBetPrediction" @play-audio=" $emit('playAudio', $event)">
        </GetBetPrediction>

        <GameResult v-else-if="activeGameState === GameStates.result" :roundResult=roundResult
            @change-active-game-state="endRound()" @play-audio=" $emit('playAudio', $event)">
        </GameResult>

        <GameOver v-else-if="activeGameState === GameStates.gameOver"
            @change-active-game-state="changeActiveGameState($event)" @play-audio="$emit('playAudio', $event)">
        </GameOver>
    </div>

    <h2 class="gamestate">Gamestate: {{ GameStates[activeGameState] }}
    </h2>
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