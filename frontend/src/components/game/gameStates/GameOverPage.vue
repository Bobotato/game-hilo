<script lang="ts" setup>
import { router } from '@/router/index'

import { GameStates } from '@/composables/hiloGame'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'changeActiveGameState', state: GameStates): void
}>()

function emitChangeGameState() {
    emit('playAudio', 'menuSelectSfx')
    emit('changeActiveGameState', 'gameOver')
}

function endGame() {
    emit('playAudio', 'menuSelectSfx')
    router.push({ path: '/mainmenu' })

}
</script>

<template>
    <div class="game-over-component">
        <h2 class="message">
            You have run out of credits. <br> Would you like to start again by providing your own "credits"?
        </h2>

        <button class="button retry" @click.once=emitChangeGameState>Retry</button>
        <button class="button leave" @click.once="endGame">Leave</button>
    </div>
</template>

<style scoped>
.game-over-component {
    display: grid;
    grid-template-rows: [message] auto [button-retry] auto [button-leave] auto;
    place-items: center;
    gap: 30px;
    width: 100vw;
}

.message {
    grid-row: message;
    text-align: center;
    line-height: 2em;
}

.button {
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
}

.button.retry {
    background-color: rgba(0, 48, 0);
}

.button.leave {
    background-color: rgba(48, 0, 0);
}

.button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    cursor: pointer;
}

.button:active {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    transform: translateY(4px);
}
</style>