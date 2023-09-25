<script lang="ts" setup>
import { ref } from 'vue'
import PokerCard from '@/components/game/gameElements/PokerCard.vue';

import { Card } from '@/types/gameElements/gameElementTypes';
import { CardRanks, CardSuits } from '@/components/gameElements/pokerCard'

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
    <div class="deck-component">
        <h2>{{ deckMessage.message }}</h2>
        <img class="deck" src="@/assets/images/CardDeck.png">
        <button class="deck-button" @click="drawCard">
            <PokerCard 
                :card=props.currentCard 
                :isStatic=false 
                @play-audio="$emit('playAudio', $event)">
            </PokerCard>
        </button>
        <button class="continue-button" @click.once="emitChangeGameState">Continue</button>
    </div>
</template>

<style scoped>
.deck-component {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    backdrop-filter: blur(5px);
}

.deck {
    width: 300px;
    height: 400px;
}

.deck-button {
    background-color: transparent;
    width: 300px;
    height: 400px;
    scale: 90%;
    transform: perspective(800px) rotateX(15deg) rotateZ(2deg);
    margin: -430px 0 60px 0;
}

.continue-button {
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