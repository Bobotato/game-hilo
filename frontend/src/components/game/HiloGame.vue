<script lang="ts" setup>
import { ref, Ref, onMounted } from 'vue'
import { AxiosError } from 'axios';

import LoadingPage from '@/components/loading/LoadingPage.vue';
import WelcomePage from '@/components/game/WelcomePage.vue'
import DrawDeckPage from '@/components/game/DrawDeckPage.vue'
import BetPage from '@/components/game/BetPage.vue';
import ResultPage from '@/components/game/ResultPage.vue';
import GameOverPage from '@/components/game/GameOverPage.vue';

import AudioController from '@/components/audioController/AudioController.vue';
import ErrorOverlay from '@/components/errorWarning/ErrorOverlay.vue';

import { useGame } from '@/composables/game/game'
import { APIServerDownError, UnauthorisedError } from '@/services/apiService/errors';
import { resetGame } from '@/services/apiService/game/game';
import { logOut } from '@/utils/logOut'
import { GameStates } from '@/models/gameStates';
import { BetPrediction } from '@/components/game/BetPage.vue';

let { roundInfo, updateRoundInfo, roundResult, updateRoundResult } = useGame()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'toggleMuteAudio'): void
}>()

interface Props {
    isMuted: Ref<boolean>
}

const props = defineProps<Props>()

let errorOverlay = ref({
    errorString: "",
})

let activeGameState: Ref<GameStates> = ref(GameStates.loading)

async function handleGetRoundInfo() {
    try {
        await updateRoundInfo()

    } catch (error: any) {
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                break
        }
    }
}

async function handleGetRoundResult(betPrediction: BetPrediction) {
    try {
        await updateRoundResult(betPrediction)
        changeActiveGameState(GameStates.result)

    } catch (error: any) {
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                break
        }
    }
}

async function startRound() {
    await handleGetRoundInfo()

    if (roundInfo.value.player.credits === 0) {
        changeActiveGameState(GameStates.gameOver)
    } else {
        changeActiveGameState(GameStates.welcome)
    }
}

async function endRound(isGameOver: boolean) {
    if (isGameOver) {
        changeActiveGameState(GameStates.gameOver)
    }
    else {
        await handleGetRoundInfo()
        changeActiveGameState(GameStates.betPrediction)
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
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                break
        }
    }
}

function logOutFromGame() {
    emit('playAudio', 'menuSelectSfx')
    try {
        logOut()

    } catch (error: any) {
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                break
            case APIServerDownError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                break
        }
    }
}

onMounted(() => {
    startRound()
})
</script>

<template>
    <ErrorOverlay
        class="game-error-overlay"
        :errorString=errorOverlay.errorString
        @play-audio="$emit('playAudio', $event)">
    </ErrorOverlay>


    <main class=game-main>
        <LoadingPage 
            v-if="activeGameState === GameStates.loading">
        </LoadingPage>

        <WelcomePage 
            v-else-if="activeGameState === GameStates.welcome" 
            :roundInfo=roundInfo
            @change-active-game-state="changeActiveGameState($event)"
            @play-audio="$emit('playAudio', $event)">
        </WelcomePage>

        <DrawDeckPage 
            v-else-if="activeGameState === GameStates.deck"
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
    </main>

    <footer class="game-footer">
        <button class="game-logout-button" @click.once=logOutFromGame>
            Log Out
        </button>

        <AudioController class="game-audio-controller"
            @toggle-mute="$emit('toggleMuteAudio')"
            :isMuted="props.isMuted">
        </AudioController>
    </footer>
</template>

<style scoped>
.game-error-overlay {
    position: absolute;
    z-index: 1000;
}

.game-main {
    margin: 50px 0 0 0;
}

.game-footer {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: auto;
    background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.05), black);
}

.game-logout-button {
    height: 50px;
    width: 250px;
    border: none;
    border-radius: 10px;
    margin: 0 0 0 5vw;
    padding: 10px;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
    background-color: rgba(0, 48, 0);
}

.game-audio-controller {
    margin: 0 2vw 0 0;
}


@media only screen and (max-width: 600px) {
.game-logout-button {
    width: 120px;
    font-size: 1.2em;
    }
}

.game-footer {
    height: 100px;
}
</style>