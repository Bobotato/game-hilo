<script lang="ts" setup>
import { Suits, Card } from '@/classes/PokerCard'


interface Props {
    card: Card
}

const props = defineProps<Props>()

function convertSymbol(suit: Suits): string {
    switch (suit) {
        case 'Spades':
            return '♠';
        case 'Diamonds':
            return '♦';
        case 'Clubs':
            return '♣';
        case 'Hearts':
            return '♥';
        default:
            return '';
    }
}

function isRed(suit: Suits): boolean {
    return (suit == "Hearts" || suit == "Diamonds")
}
</script>
<template>
    <div class="card">
        <div :class="{ 'rank red': isRed(props.card.suit), 'rank': isRed(props.card.suit) == false }">{{
            props.card.rank }}</div>
        <div :class="{ 'suit red': isRed(props.card.suit), 'suit': isRed(props.card.suit) == false }">{{
            convertSymbol(props.card.suit) }}</div>
        <div :class="{ 'rank-bottom red': isRed(props.card.suit), 'rank-bottom': isRed(props.card.suit) == false }">{{
            props.card.rank }}</div>
    </div>
</template>
  
<style>
.card {
    display: grid;
    grid-template-rows: [rank] auto [suit] auto [rank-bottom] auto;
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

.rank-bottom {
    grid-row: rank-bottom;
    margin: 0 20px 20px 0;
    font-size: 3em;
    transform: rotate(180deg);
}

.suit {
    width: 200px;
    grid-row: suit;
    font-size: 10em;
    text-align: center;
    margin: -0.2em 0 -0.5em 0;
}

.red {
    color: rgb(139, 0, 0);
}
</style>