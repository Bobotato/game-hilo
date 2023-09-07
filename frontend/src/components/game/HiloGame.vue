<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { router } from '@/router/index'

import DrawDeck from '@/components/game/gameElements/DrawDeck.vue'
import GetBetPrediction from '@/components/game/gameElements/GetBetPrediction.vue';
import StartMessage from '@/components/game/gameElements/StartMessage.vue';
import GameResult from '@/components/game/gameElements/GameResult.vue';
import WelcomeScreen from '@/components/game/gameElements/WelcomeScreen.vue'
import GameOverScreen from '@/components/game/gameElements/GameOverScreen.vue';

import { Prediction } from '@/composables/gameElements/getBetPrediction';
import { Token } from '@/services/apiService/game/game';

import { useRoundInfoComposable, useRoundResultComposable, GameStates } from '@/composables/hiloGame'
import { UnauthorisedError } from '@/services/apiService/errors';

let { roundInfo, updateRoundInfo } = useRoundInfoComposable()
let { roundResult, updateRoundResult } = useRoundResultComposable()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

const token = { access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2OTQwNzQ2OTd9.X7WlktInEr0-gYSfGkYa4k34mSc7qXiKXGWqtfx24lY" }

let errorMessage = ref({
    message: "",
    isShowing: false
})

let activeGameState = ref(GameStates.start)

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

async function handleGetRoundResult(token: Token, bet: Bet, prediction: Prediction) {
    try {
        await updateRoundResult(token, bet, prediction)
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

async function startRound(token: Token) {
    try {
        activeGameState.value = GameStates.welcome
        await handleGetRoundInfo(token)
    } catch (error) {
        console.log(error)
    }
}

async function submitBetPrediction(bet: number, prediction: number) {
    console.log(`Player bet ${bet}`)
    console.log(`Player predicted ${Prediction[prediction]}`)
    await handleGetRoundResult(token, bet, prediction)
    activeGameState.value = GameStates.result
}

async function endRound(token: Token) {
    try {
        activeGameState.value = GameStates.betPrediction
        await handleGetRoundInfo(token)
    } catch (error) {
        console.log(error)
    }
}

function endGame() {
    router.push({ path: '/mainmenu' })
}

onMounted(() => {
    handleGetRoundInfo(token)
})

function changeActiveGameState(gamestate: GameStates) {
    activeGameState.value = gamestate
}

</script>

<template>
    <div class=game>
        <StartMessage class=start-message-component v-if="activeGameState === GameStates.start"
            @play-audio="$emit('playAudio', $event)" @change-active-game-state="startRound(token)">
        </StartMessage>

        <WelcomeScreen class="welcome-screen-component" v-if="activeGameState === GameStates.welcome"
            :name=roundInfo.player.name :credits=roundInfo.player.credits
            @change-active-game-state="activeGameState = GameStates.deck" @play-audio="$emit('playAudio', $event)">
        </WelcomeScreen>

        <DrawDeck class=draw-deck-component v-else-if="activeGameState === GameStates.deck"
            :currentCard=roundInfo.current_card @play-audio="$emit('playAudio', $event)"
            @change-active-game-state="activeGameState = GameStates.betPrediction">
        </DrawDeck>

        <GetBetPrediction v-else-if="activeGameState === GameStates.betPrediction"
            @submit-bet-prediction="submitBetPrediction" @play-audio=" $emit('playAudio', $event)" :roundInfo=roundInfo>
        </GetBetPrediction>

        <GameResult v-else-if="activeGameState === GameStates.result" :roundResult=roundResult
            @change-active-game-state="endRound(token)" @play-audio=" $emit('playAudio', $event)">
        </GameResult>

        <GameOverScreen v-else-if="activeGameState === GameStates.gameOver"
            @change-active-game-state="changeActiveGameState($event)" @play-audio="$emit('playAudio', $event)"
            @end-game="endGame">
        </GameOverScreen>
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