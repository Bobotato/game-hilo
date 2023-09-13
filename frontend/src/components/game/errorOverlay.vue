<script lang="ts" setup>
import { router } from '@/router/index'

interface Props {
    error: string
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

function returnToLogin() {
    emit('playAudio', 'menuSelectSfx')
    router.push({ path: '/login' })
}
</script>

<template>
    <div class="backdrop-filter">
    </div>

    <div class="error-overlay-component">
        <img class="error-icon" src="@/assets/images/errorIcon.svg">
        <h2 class="message">An error has occured: <br> {{ props.error }}</h2>
        <button class="button" @click.once="returnToLogin">Return to Login</button>
    </div>
</template>

<style scoped>
.backdrop-filter {
    z-index: 1000;
    backdrop-filter: blur(10px) grayscale(50%);
    background-color: rgba(0, 0, 0, 0.5);
    position: absolute;
    width: 100%;
    height: 100%;
}

.error-overlay-component {
    position: absolute;
    z-index: 1000;
    display: grid;
    grid-template-rows: [icon] auto [message] auto [button] auto;
    gap: 30px;
    place-items: center;
    width: 100%;
}

.error-icon {
    grid-row: icon;
    width: 50px;
    height: 50px;
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