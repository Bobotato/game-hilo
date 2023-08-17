<script lang="ts" setup>
import { ref } from 'vue'

import CardInventory from '@/components/game/gameElements/CardInventory.vue'
import ReceiveItem from '@/components/game/gameElements/ReceiveItem.vue'
import GetBetPrediction from './gameElements/GetBetPrediction.vue';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()


let currentCredits = ref(0)

let gameMessage = ref({
    message: `Welcome back to the game. \n You have ${currentCredits.value} "credits".`,
    isShowing: true
})

function toggleGameMessage() {
    gameMessage.value.isShowing = !gameMessage.value.isShowing
    emit('playAudio', 'menuSelectSfx')
}
</script>

<template>
    <div class="game">
        <!-- <div v-if=gameMessage.isShowing class="game-message-card">
            <h2 class="game-message">{{ gameMessage.message }}</h2>
            <button class="game-message-button" @click=toggleGameMessage()>Ok</button>
        </div> -->
        <GetBetPrediction @play-audio="$emit('playAudio', $event)" currentCard="test" :currentCredits=currentCredits>
        </GetBetPrediction>
        <!-- <ReceiveItem v-if=!gameMessage.isShowing class=game-events :itemName="`tester`"
            :item-image-source="`../../../assets/images/Fingers.png`">
        </ReceiveItem>

        <h2 class="inventory-credits">Remaining "Credits": {{ currentCredits }}</h2>

        <CardInventory v-if=!gameMessage.isShowing class="inventory-cards"></CardInventory> -->
    </div>
</template>

<style>
.game {
    display: grid;
    width: 100vw;
    height: 100vh;
    grid-template-rows: [game-events] auto [game-misc] auto;
    grid-template-columns: [left] 1fr [middle] 1fr [right] 1fr;
}

.game-message-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 30vh;
    grid-row: game-events;
    grid-column: middle;
}

.game-message {
    white-space: pre-wrap;
    line-height: 2em;
    text-align: center;
}

.game-message-button {
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
    background-color: rgba(48, 0, 0, 80%);
}


.game-events {
    grid-row: game-events;
    grid-column: middle;
    background: rgba(255, 0, 0, 0.235);
}

.inventory-credits {
    grid-row: game-misc;
    grid-column: left;
    align-self: end;
    padding: 0 0 5vh 5vw;
}

.inventory-cards {
    grid-row: game-misc;
    grid-column: middle;
    justify-self: center;
    align-self: end;
    margin: 0 0 5vh 0;
}
</style>