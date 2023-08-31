<script lang="ts" setup>
import { ref } from 'vue'
import PokerCard from '@/components/game/gameElements/PokerCard.vue';

import { Card } from '@/types/gameElements/gameElementTypes';

interface Props {
    currentCard: Card
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'drawCard'): void
    (e: 'playAudio', sound: string): void
}>()

let deckMessage = ref({
    message: "Draw a card to begin.",
    isShowing: true
})

function emitDrawCard() {
    emit('playAudio', 'choiceSelectSfx')
    emit('drawCard')
}

</script>

<template>
    <div class="bg-filter">
        <PokerCard :card=props.currentCard @play-audio="$emit('playAudio', $event)"></PokerCard>





        // <!-- <h2>{{ deckMessage.message }}</h2>
        // <img class="deck" src="@/assets/images/CardDeck.png">
        // <button class="deck-button" @click.once="emitDrawCard"></button> -->
    </div>
</template>

<style scoped>
.deck {
    width: 300px;
    height: 400px;
}

.deck-button {
    position: absolute;
    background-color: transparent;
    width: 240px;
    height: 360px;
    border-radius: 10px;
    background-image: url("@/assets/images/cardRearBackground.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-color: #cccccc00;
    box-shadow: 0px 0px 5px rgba(48, 48, 44, 0.8);
    transform: perspective(800px) rotateX(15deg) rotateZ(2deg);
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