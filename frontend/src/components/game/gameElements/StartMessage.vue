<script lang="ts" setup>
import { ref, Ref } from 'vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'startGame'): void
}>()

interface Message {
    message: string
    isShowing: boolean
}

let message: Ref<Message> = ref({
    message: "Welcome back to the game.",
    isShowing: true
})

function emitStartGame() {
    toggleMessage()
    emit('startGame')
}

function toggleMessage() {
    emit('playAudio', 'menuSelectSfx')
    message.value.isShowing = !message.value.isShowing
}
</script>

<template>
    <div class="bg-filter" v-if=message.isShowing>
        <h2 class="game-message">{{ message.message }}</h2>
        <button class="acknowledge-button" @click.once=(emitStartGame)>Start Game</button>
    </div>
</template>

<style>
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