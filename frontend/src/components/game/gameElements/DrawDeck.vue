<script lang="ts" setup>
import { ref } from 'vue'
import PokerCard from '@/components/game/gameElements/PokerCard.vue';

import { Card } from '@/types/gameElements/gameElementTypes';
import { CardRanks, CardSuits } from '@/services/card'

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
    <div class="bg-filter">
        <h2>{{ deckMessage.message }}</h2>
        <img class="deck" src="@/assets/images/CardDeck.png">
        <button class="deck-button" @click="drawCard">
            <PokerCard :card=props.currentCard :isStatic=false @play-audio="$emit('playAudio', $event)"></PokerCard>
        </button>
        <button class="continue-button" @click.once="emitChangeGameState">Continue</button>
    </div>
</template>

<style scoped>
.deck {
    width: 300px;
    height: 400px;
}

.deck-button {
    background-color: transparent;
    width: 300px;
    height: 400px;
    scale: 90%;
    transform: perspective(800px) rotateX(15deg);
    margin: -430px 0 30px 0;
}

.deck-button:hover {
    box-shadow: 0px 0px 5px rgba(48, 48, 44, 0.8);
}

.bg-filter {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    backdrop-filter: blur(5px);
}
</style>