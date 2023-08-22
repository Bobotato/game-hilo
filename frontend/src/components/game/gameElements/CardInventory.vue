<script lang="ts" setup>
import { ref } from 'vue'
import PokerCard from '@/components/game/gameElements/PokerCard.vue';

let isEmpty = ref(false)
</script>

<template>
    <div class=inventory v-if="!isEmpty">
        <h2 class=inventory-label>Your card:</h2>
        <PokerCard></PokerCard>
    </div>
</template>

<style>
.inventory {
    display: grid;
    grid-template-rows: [inventory-label] auto [inventory-items] auto;
    align-items: center;
    justify-content: center;
}

.inventory-label {
    grid-row: inventory-label;
    text-justify: center;
    justify-self: center;
}
</style>