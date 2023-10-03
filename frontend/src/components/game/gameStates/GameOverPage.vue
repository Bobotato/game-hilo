<script lang="ts" setup>
import { router } from '@/router/index'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'isRetrying'): void
}>()

function retry() {
    emit('playAudio', 'restartGameSfx')
    emit('isRetrying')
}

function endGame() {
    emit('playAudio', 'menuSelectSfx')
    router.push({ path: '/mainmenu' })
}
</script>

<template>
    <div class="game-over-main">
        <h2 class="game-over-message">
            You have run out of credits. <br> Would you like to start again by providing your own "credits"?
        </h2>

        <div class="game-over-spotlight"></div>

        <button class="game-over-button_retry" @click.once="retry"></button>

        <button class="game-over-button game-over-button_leave" @click.once="endGame">Leave</button>
    </div>
</template>

<style scoped>
.game-over-main {
    display: grid;
    grid-template-rows: [message] auto [button-retry] auto [button-leave] auto;
    place-items: center;
    gap: 30px;
    width: 100vw;
}

.game-over-message {
    grid-row: message;
    text-align: center;
    line-height: 2em;
}

.game-over-restart-button-wrapper {
    grid-row: button-retry;
}

.game-over-button_retry {
    aspect-ratio: 4/7;
    height: 700px;
    background: transparent;
    background-image: url("@/assets/images/restartButton.png");
    z-index: 1;
}

.game-over-button_retry:hover {
  box-shadow: none;
  cursor: pointer;
}

.game-over-button_retry:active {
  box-shadow: none;
  transform: none;
}

.game-over-spotlight {
    position: absolute;
    top: 70%;
    height: 100px;
    width: 700px;
    margin: 5vh 0 0 0;
    background-color: rgba(255, 241, 200, 0.3);
    filter: blur(20px);
    border-radius: 50%;
}

.game-over-button {
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

.game-over-button_leave {
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