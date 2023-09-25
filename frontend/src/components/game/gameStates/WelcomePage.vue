<script lang="ts" setup>
import { GameStates } from '@/composables/hiloGame'
import { RoundInfo } from '@/types/gameElements/gameElementTypes';

interface Props {
    roundInfo: RoundInfo
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'changeActiveGameState', state: GameStates): void
}>()


function emitChangeGameState() {
    emit('playAudio', 'creditPickupSfx')
    emit('changeActiveGameState', GameStates["deck"])
}
</script>

<template>
    <div class="welcome-component">
        <h2 class="message">Welcome back, {{ props.roundInfo.player.name }}. <br> You currently have {{
            props.roundInfo.player.credits }}
            "credits". <br><br> Take your credits.
        </h2>
        <button class="take-credit-button floating" alt="Credits" @click.once=(emitChangeGameState)>
        </button>
        <div class="shadow darkening"></div>
    </div>
</template>

<style>
.welcome-component {
    display: grid;
    grid-template-rows: [message] auto [image] auto [shadow] auto;
    place-items: center;
    gap: 30px;
    width: 100%;
}

.message {
    grid-row: message;
    text-align: center;
    font-size: 1.5em;
    line-height: 2em;
}

.take-credit-button {
    grid-row: image;
    height: 300px;
    width: 400px;
    background: transparent;
    background-image: url("@/assets/images/Fingers.png");
    background-repeat: no-repeat;
    background-size: cover;
}

.take-credit-button:hover {
    cursor: grab;
}

.item-image {
    grid-row: image;
    height: 300px;
}

.floating {
    animation-name: floating;
    animation-duration: 2s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
}

@keyframes floating {
    0% {
        transform: translate(0, 0px);
    }

    50% {
        transform: translate(0, 10px);
    }

    100% {
        transform: translate(0, -0px);
    }
}

.shadow {
    height: 50px;
    width: 400px;
    margin: 5vh 0 0 0;
    background-color: #0800008f;
    filter: blur(6px);
    border-radius: 50%;
}

.darkening {
    animation-name: darkening;
    animation-duration: 2s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
}

@keyframes darkening {
    0% {
        background-color: #08000062;
    }

    50% {
        background-color: #0800009f;
    }

    100% {
        background-color: #08000062;
    }
}
</style>@/composables/game/hiloGame