<script lang='ts' setup>
import PokerCard from '@/components/game/gameElements/PokerCard.vue';

import { RoundResult } from '@/types/gameElements/gameElementTypes';
import { CardRanks, CardSuits } from '@/models/pokerCard';


interface Props {
    roundResult: RoundResult
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'endRound', isGameOver: boolean): void
    (e: 'playAudio', sound: string): void
}>()

function emitEndRound() {
    emit('playAudio', 'menuSelectSfx')
    emit('endRound', props.roundResult.is_player_bankrupt)
}
</script>

<template>
    <main class="game-result">
        <h2 class="drawn-card-message">The drawn card was:</h2>

        <PokerCard class="drawn-card" :card=props.roundResult.drawn_card :isStatic="true"></PokerCard>

        <h2 class="result-message win" v-if="props.roundResult.win">You have won. <br /> You survive another round.</h2>
        <h2 class="result-message lose" v-if="!props.roundResult.win">You have lost.</h2>

        <button class="continue-button" @click.once="emitEndRound">
            Continue
        </button>
    </main>
</template>

<style scoped>
.game-result {
    display: grid;
    grid-template-rows: [drawn-card-message] auto [drawn-card] auto [result-message] auto [continue-button] auto;
    place-items: center;
    align-self: center;
}

.drawn-card-message {
    font-size: 1.5em;
    grid-row: drawn-card-message;
}

.drawn-card {
    grid-row: drawn-card;
    width: 300px;
    height: 400px;
    margin: 20px 0;
}

.result-message {
    font-size: 1.5em;
    grid-row: result-message;
    text-align: center;
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

@media only screen and (max-width: 600px) {
.drawn-card-message {
    font-size: 1.2em;
}

.drawn-card {
    width: 210px;
    height: 280px;
}

.drawn-card-string {
    font-size: 1.2em;
}

.result-message {
    font-size: 1.2em;
}

.continue-button {
    font-size: 1.2em;
}


}
</style>