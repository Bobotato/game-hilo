<script lang='ts' setup>
import PokerCard from '@/components/game/gameElements/PokerCard.vue';

import { Card } from '@/classes/PokerCard';

interface Props {
    drawnCard: Card
    isWin: boolean
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'acceptResult'): void
    (e: 'playAudio', sound: string): void
}>()
</script>

<template>
    <div class="game-result">
        <h2 class="drawn-card-message">The drawn card was:</h2>

        <PokerCard class="drawn-card" :card=props.drawnCard></PokerCard>

        <h2 class="drawn-card-string">{{ drawnCard.toString() }}</h2>

        <h2 class="result-message win" v-if="isWin">You have won.</h2>
        <h2 class="result-message win" v-if="!isWin">You have lost.</h2>

        <button class="continue-button">
            Continue
        </button>
    </div>
</template>

<style>
.game-result {
    display: grid;
    grid-template-rows: [drawn-card-message] auto [drawn-card] auto [drawn-card-string] auto [result-message] auto [continue-button] auto;
    width: 100%;
    height: 50%;
    place-items: center;
    align-self: center;
}

.drawn-card-message {
    grid-row: drawn-card-message;
}

.drawn-card {
    grid-row: drawn-card;
}

.drawn-card-string {
    grid-row: drawn-card-string;
}

.result-message {
    grid-row: result-message;
}

.continue-button {
    grid-row: continue-button;
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
    margin: 25px 0 0 0;
    background-color: rgba(0, 48, 0);
}
</style>