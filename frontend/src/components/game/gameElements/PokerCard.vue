<script lang="ts" setup>
import { Ranks, Suits, Card } from '@/classes/PokerCard'


interface Props {
    card?: Card
}

const props = withDefaults(defineProps<Props>(), {
    card: () => new Card(Suits.Spades, Ranks.A)
})

function convertSymbol(suit: Suits) {
    switch (suit) {
        case 0:
            return '♠';
        case 1:
            return '♦';
        case 2:
            return '♣';
        case 3:
            return '♥';
        default:
            return '';
    }
}

function isRed(suit: Suits) {
    if (suit == 1 || suit == 3) {
        return true
    } else {
        return false
    }
}
</script>
<template>
    <div class="card">
        <div :class="{ 'rank red': isRed(props.card.suit), 'rank': isRed(props.card.suit) == false }">{{
            Ranks[props.card.rank] }}</div>
        <div :class="{ 'suit red': isRed(props.card.suit), 'suit': isRed(props.card.suit) == false }">{{
            convertSymbol(props.card.suit) }}</div>
    </div>
</template>
  
<style>
.card {
    display: grid;
    grid-template-rows: [rank] 1fr [suit] 4fr;
    width: 200px;
    height: 300px;
    background: url("@/assets/images/CardBackground.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.55) 0px 3px 8px;
}

.rank {
    grid-row: rank;
    margin: 20px 0 0 20px;
    font-size: 3em;
}

.suit {
    width: 200px;
    grid-row: suit;
    font-size: 10em;
    text-align: center;
}

.red {
    color: rgb(139, 0, 0);
}
</style>