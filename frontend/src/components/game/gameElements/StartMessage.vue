<script lang="ts" setup>
import { ref, Ref } from 'vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'changeActiveGameState', state: string): void
}>()

interface Message {
    message: string
    isShowing: boolean
}

let message: Ref<Message> = ref({
    message: "Welcome back to the game.",
    isShowing: true
})

function emitChangeGameState() {
    emit('playAudio', 'menuSelectSfx')
    emit('changeActiveGameState', "welcome-screen-component")
}
</script>

<template>
    <div class="bg-filter" v-if=message.isShowing>
        <h2 class="game-message">{{ message.message }}</h2>
        <button class="acknowledge-button" @click.once=emitChangeGameState>Start Game</button>
    </div>
</template>

<style>
.bg-filter {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(5px);
    width: 100%;
    height: 100%;
}

.acknowledge-button {
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
</style>