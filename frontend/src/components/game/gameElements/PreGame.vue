<script lang="ts" setup>
import { GameStates } from '@/composables/hiloGame'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'changeActiveGameState', state: GameStates): void
    (e: 'startGame'): void
}>()

function emitStartGame() {
    emit('playAudio', 'menuSelectSfx')
    emit('changeActiveGameState', GameStates["welcome"])
    emit('startGame')
}
</script>

<template>
    <div class="pre-game-component">
        <h2 class="message">Welcome back to the game.</h2>
        <button class="button" @click.once=emitStartGame>Start Game</button>
    </div>
</template>

<style scoped>
.pre-game-component {
    display: grid;
    grid-template-rows: [message] auto [button] auto;
    gap: 30px;
    place-items: center;
    width: 100%;
}

.message {
    grid-row: message;
    text-align: center;
    font-size: 1.5em;
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