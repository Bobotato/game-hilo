<script lang="ts" setup>
import { RoundInfo } from '@/types/gameElements/gameElementTypes';
import { ref, Ref } from 'vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'startGame'): void
}>()

interface Props {
    roundInfo: RoundInfo
}

const props = defineProps<Props>()

function emitStartGame() {
    emit('startGame')
}
</script>

<template>
    <div class="bg-filter">
        <h2 class="game-message">Welcome back to the game {{ props.roundInfo.player.name }}</h2>
        <h2 class="game-message">You currently have {{ props.roundInfo.player.credits }} "credits".</h2>
        <button class="acknowledge-button" @click.once=(emitStartGame)>Start Game</button>
    </div>
    <div class="receive-item-wrapper">
        <div class="receive-item-card">
            <h2 class="item-receive-text">You have received:</h2>
            <div class="item-wrapper">
                <img class="item-image" src="@/assets/images/fingers.png" :alt="'Credits'">
                <h2 class="item-receive-text">10</h2>
            </div>
        </div>
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

<!-- <script lang="ts" setup>

</script>

<style>
.receive-item-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
}

.receive-item-card {
    display: grid;
    grid-template-rows: [item-receive-text] auto [item-image] auto [item-receive-qty] auto [item-name] auto;
    align-items: center;
    justify-content: center;
    width: 1000px;
}

.item-receive-text {
    text-align: center;
    font-size: 1.5em;
    color: white;
}

.item-image {
    height: 300px;
}

.item-desc {
    text-align: center;
    font-size: 1.5em;
    color: white;
}
</style> -->