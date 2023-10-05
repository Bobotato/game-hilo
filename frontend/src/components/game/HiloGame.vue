<script lang="ts" setup>
import { ref, Ref } from 'vue'
import { AxiosError } from 'axios';

import LoadingPage from '@/components/loading/LoadingPage.vue';
import WelcomePage from '@/components/game/gameStates/WelcomePage.vue'
import DrawDeckPage from '@/components/game/gameStates/DrawDeckPage.vue'
import BetPage from '@/components/game/gameStates/BetPage.vue';
import ResultPage from '@/components/game/gameStates/ResultPage.vue';
import GameOverPage from '@/components/game/gameStates/GameOverPage.vue';

import ErrorOverlay from '@/components/errorWarning/ErrorOverlay.vue';

import { useGame } from '@/composables/game/game'
import { APIServerDownError, UnauthorisedError } from '@/services/apiService/errors';
import { resetGame } from '@/services/apiService/game/game';
import { logOut } from '@/utils/logOut'
import { GameStates } from '@/models/gameStates';
import { BetPrediction } from '@/components/game/gameStates/BetPage';

let { roundInfo, updateRoundInfo, roundResult, updateRoundResult } = useGame()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let errorOverlay = ref({
    errorString: "",
})

let activeGameState: Ref<GameStates> = ref(GameStates.loading)

async function handleGetRoundInfo() {
    try {
        await updateRoundInfo()
    } catch (error: any) {
        console.error(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                console.error(error.message)
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                console.error(error.message)
                break
        }
    }
}

async function handleGetRoundResult(betPrediction: BetPrediction) {
    try {
        await updateRoundResult(betPrediction)
        changeActiveGameState(GameStates.result)
    } catch (error: any) {
        console.error(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                console.error(error.message)
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                console.error(error.message)
                break
        }
    }
}

async function startRound() {
    try {
        await handleGetRoundInfo()
        if (roundInfo.value.player.credits === 0) {
            changeActiveGameState(GameStates.gameOver)
        } else {
            changeActiveGameState(GameStates.welcome)
        }
    } catch (error) {
        console.error(error)
    }
}

async function endRound(isGameOver: boolean) {
    try {
        if (isGameOver) {
            changeActiveGameState(GameStates.gameOver)
        }
        else {
            await handleGetRoundInfo()
            changeActiveGameState(GameStates.betPrediction)
        }
    } catch (error) {
        console.error(error)
    }
}

function changeActiveGameState(gamestate: GameStates) {
    activeGameState.value = gamestate
}

function restartGame() {
    try {
        resetGame()
        handleGetRoundInfo()
        changeActiveGameState(GameStates.welcome)
    } catch (error: any) {
        console.error(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                console.error(error.message)
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                console.error(error.message)
                break
        }
    }
}

function logOutFromGame() {
    emit('playAudio', 'menuSelectSfx')
    try {
        logOut()
    } catch (error: any) {
        console.error(error)
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                console.error(error.message)
                break
            case APIServerDownError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                console.error(error.message)
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                console.error(error.message)
                break
    }
}
}

startRound()
</script>

<template>
    <div class=game-main>
        <ErrorOverlay 
            :errorString=errorOverlay.errorString
            @play-audio="$emit('playAudio', $event)">
        </ErrorOverlay>

        <LoadingPage
            v-if="activeGameState === GameStates.loading">
        </LoadingPage>

        <WelcomePage
            v-if="activeGameState === GameStates.welcome" 
            :roundInfo=roundInfo
            @change-active-game-state="changeActiveGameState($event)"
            @play-audio="$emit('playAudio', $event)">
        </WelcomePage>

        <DrawDeckPage
            v-if="activeGameState === GameStates.deck"
            :currentCard=roundInfo.current_card
            @play-audio="$emit('playAudio', $event)"
            @change-active-game-state="activeGameState = GameStates.betPrediction">
        </DrawDeckPage>

        <BetPage
            v-else-if="activeGameState === GameStates.betPrediction"
            :roundInfo=roundInfo
            @submit-bet-prediction="handleGetRoundResult($event)"
            @play-audio=" $emit('playAudio', $event)">
        </BetPage>

        <ResultPage
            v-else-if="activeGameState === GameStates.result" 
            :roundResult=roundResult @endRound="endRound($event)"
            @play-audio=" $emit('playAudio', $event)">
        </ResultPage>

        <GameOverPage 
            v-else-if="activeGameState === GameStates.gameOver"
            @is-retrying="restartGame()"
            @play-audio="$emit('playAudio', $event)">
        </GameOverPage>
    </div>


    <button class="game-logout-button" @click.once=logOutFromGame>Log Out</button>
</template>

<style scoped>
.game-main {
    display: grid;
    width: 100vw;
    height: 100vh;
    place-items: center;
}

.game-logout-button {
    position: absolute;
    left: 3%;
    bottom: 4%;
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