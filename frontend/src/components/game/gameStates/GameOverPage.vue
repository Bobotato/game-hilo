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
    <main class="game-over-main">
        <p class="game-over-message">
            You have run out of credits. <br> Would you like to start again by providing your own "credits"?
        </p>

        <button class="game-over-button_retry" @click.once="retry"></button>

        <button class="game-over-button game-over-button_leave" @click.once="endGame">Leave</button>
    </main>
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
    white-space: pre-wrap;
    text-align: center;
    font-size: 1.5em;
    color: white;
    grid-row: message;
    text-align: center;
    line-height: 2em;
}

.game-over-restart-button-wrapper {
    grid-row: button-retry;
}

.game-over-button_retry {
    width: 400px;
    height: 700px;
    background: transparent;
    background-image: url("@/assets/images/restartButton.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
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

@media only screen and (max-width: 600px) {
.game-over-button_retry {
    width: 200px;
    height: 350px;
    }
.game-over-button {
    font-size: 1.2em;
 }

.game-over-message {
    font-size: 1.2em;
}
}
</style>