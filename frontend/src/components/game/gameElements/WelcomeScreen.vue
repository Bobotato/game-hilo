<script lang="ts" setup>
const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'changeActiveGameState'): void
}>()

interface Props {
    name: string,
    credits: number
}

const props = defineProps<Props>()

function emitChangeGameState() {
    emit('playAudio', 'creditPickupSfx')
    emit('changeActiveGameState')
}
</script>

<template>
    <div class="welcome-component">
        <h2 class="welcome-message">Welcome back, {{ props.name }}.</h2>
        <h2 class="welcome-message-2">You currently have {{ props.credits }} "credits".</h2>
        <h2 class="take-credit-prompt">Take your credits.</h2>
        <button class="take-credit-button" alt="Credits" @click.once=(emitChangeGameState)>
        </button>
    </div>
</template>

<style>
.welcome-component {
    display: grid;
    grid-template-rows: [welcome-message] auto [welcome-message-2] auto [take-credit-prompt] auto [image] auto;
    place-items: center;
}

.welcome-message {
    grid-row: welcome-message;
    text-align: center;
    font-size: 1.5em;
    color: white;
}

.welcome-message-2 {
    grid-row: welcome-message-2;
    text-align: center;
    font-size: 1.5em;
    color: white;
}

.take-credit-prompt {
    grid-row: take-credit-prompt;
    text-align: center;
    font-size: 1.5em;
    color: white;
    margin-bottom: 50px;
}

.take-credit-button {
    grid-row: image;
    height: 300px;
    width: 400px;
    color: white;
    background-image: url("@/assets/images/Fingers.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-color: #cccccc00;
}

.take-credit-button:hover {
    cursor: grab;
}

.item-image {
    grid-row: image;
    height: 300px;
}
</style>