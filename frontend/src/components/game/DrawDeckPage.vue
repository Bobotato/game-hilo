<script lang="ts" setup>
import { ref } from 'vue'

import PokerCard from '@/components/game/PokerCard.vue';

import { Card } from '@/types/gameElements/gameElementTypes';
import { CardRanks, CardSuits } from '@/models/pokerCard'

interface Props {
    currentCard: Card
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'changeActiveGameState'): void
    (e: 'playAudio', sound: string): void
}>()

let deckMessage = ref({
    message: "Draw a card to begin.",
    isShowing: true
})

function drawCard() {
    deckMessage.value.message = `Your card is the ${CardRanks[props.currentCard.rank]} of ${CardSuits[props.currentCard.suit]}.`
}

function emitChangeGameState() {
    emit('playAudio', 'menuSelectSfx')
    emit('changeActiveGameState')
}

</script>

<template>
    <main class="draw-deck-main">
        <div class="deck-wrapper">
            <p class="deck-message">{{ deckMessage.message }}</p>

            <button class="deck-button"
                    @click="drawCard">
                <PokerCard 
                    :card=props.currentCard 
                    :isStatic=false 
                    @play-audio="$emit('playAudio', $event)">
                </PokerCard>
            </button>

            <button class="deck-continue-button" @click.once="emitChangeGameState">Continue</button>
        </div>

        <img class="deck-image" src="@/assets/images/CardDeck.png">
    </main>
</template>

<style scoped>
.draw-deck-main {
    display: grid;
    place-items: center;
    height: 100%;
    width: 100%;
}

.deck-wrapper {
    display: grid;
    grid-template-rows: [deck-message] auto [draw-deck] auto [deck-continue-button] auto;
    place-items: center;
}

.deck-message {
    grid-row: deck-message;
    white-space: pre-wrap;
    text-align: center;
    font-size: 1.5em;
    color: white;
}

.deck-image {
    position: absolute;    
    width: 300px;
    height: 400px;
}

.deck-button {
    z-index: 1;
    grid-row: draw-deck;
    background-color: transparent;
    width: 270px;
    height: 360px;
    margin: 40px 0 65px 0;
}

.deck-continue-button {
    grid-row: deck-continue-button;
    height: 50px;
    width: 250px;
    border: none;
    border-radius: 10px;
    padding: 10px;
    margin: 20px 0;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
    background-color: rgba(48, 0, 0);
}

@media only screen and (max-width: 600px) {
.deck-message {
    width: 90%;
    font-size: 1.2em;
}

.deck-image {
    width: 225px;
    height: 300px;
}

.deck-button {
    width: 210px;
    height: 280px;
    margin: 20px 0 30px 0;
}

.deck-continue-button {
    font-size: 1.2em;
}
}
</style>