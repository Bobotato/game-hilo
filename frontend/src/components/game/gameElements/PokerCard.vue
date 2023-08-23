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
        <div class=top-symbol>
            <div :class="{ 'rank rank-top red': isRed(props.card.suit), 'rank rank-top': isRed(props.card.suit) == false }">
                {{
                    props.card.rank }}</div>

            <div
                :class="{ 'minisuit suit-top red': isRed(props.card.suit), 'minisuit suit-top': isRed(props.card.suit) == false }">
                {{ convertSymbol(props.card.suit) }}</div>
        </div>

        <div :class="{ 'suit red': isRed(props.card.suit), 'suit': isRed(props.card.suit) == false }">{{
            convertSymbol(props.card.suit) }}</div>

        <div class=bottom-symbol>
            <div
                :class="{ 'minisuit suit-bottom red': isRed(props.card.suit), 'minisuit suit-bottom': isRed(props.card.suit) == false }">
                {{ convertSymbol(props.card.suit) }}</div>

            <div
                :class="{ 'rank rank-bottom red': isRed(props.card.suit), 'rank rank-bottom': isRed(props.card.suit) == false }">
                {{ props.card.rank }}</div>
        </div>
    </div>
</template>
  
<style>
.card {
    display: grid;
    grid-template-rows: [top-symbol] auto [suit] auto [bottom-symbol] auto;
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
    font-size: 2em;
    font-weight: bold;
    letter-spacing: -0.1em;
}

.minisuit {
    font-size: 2em;
    font-weight: bold;
    letter-spacing: -0.1em;
}

.top-symbol {
    display: grid;
    place-items: center;
    width: 1em;
    grid-template-rows: [rank-top] 2em [suit-top] 2em;
    margin: 1em 0 0 1em;
}

.suit-top {
    grid-row: suit-top;
}

.rank-top {
    grid-row: rank-top;
}

.bottom-symbol {
    display: grid;
    place-items: center;
    width: 1em;
    grid-template-rows: [rank-bottom] 2em [suit-bottom] 2em;
    margin: 0 1em 1em 0;
    transform: rotate(180deg);
    justify-self: end;
}

.suit-bottom {
    grid-row: suit-bottom;
}

.rank-bottom {
    grid-row: rank-bottom;
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