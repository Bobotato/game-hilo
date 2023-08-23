<script lang="ts" setup>
import { ref } from 'vue'

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
        <h2>{{ deckMessage.message }}</h2>
        <img class="deck" src="@/assets/images/CardDeck.png">
        <button class="deck-button" @click.once="emitDrawCard"></button>
    </div>
</template>

<style scoped>
.deck {
    width: 20vw;
    height: 40vh;
}

.deck-button {
    position: absolute;
    background-color: transparent;
    width: 15vw;
    height: 35vh;
}

.deck-button:hover {
    box-shadow: none;
}

.bg-filter {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    backdrop-filter: blur(5px);
}
</style>