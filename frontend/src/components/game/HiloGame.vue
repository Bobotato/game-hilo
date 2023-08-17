<script lang="ts" setup>
import { ref } from 'vue'

import CardInventory from '@/components/game/gameElements/CardInventory.vue'
import ReceiveItem from '@/components/game/gameElements/ReceiveItem.vue'

let currentCredits = ref(0)
</script>

<template>
    <div class="game">
        <ReceiveItem v-if=true class=game-events :itemName="`tester`"
            :item-image-source="`../../../assets/images/Fingers.png`">
        </ReceiveItem>

        <h2 class="inventory-credits">Remaining "Credits": {{ currentCredits }}</h2>

        <CardInventory class="inventory-cards"></CardInventory>
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

.mute-button {
    grid-row: game-misc;
    grid-column: right;
}
</style>