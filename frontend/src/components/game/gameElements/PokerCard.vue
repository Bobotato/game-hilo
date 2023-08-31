<script lang="ts" setup>
import { ref } from 'vue'
import { Card } from '@/types/gameElements/gameElementTypes';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

interface Props {
    card: Card
}

let isCardFlipped = ref(false)

const props = defineProps<Props>()

function convertSymbol(card: Card): string {
    switch (card.suit) {
        case 1:
            return '♦';
        case 2:
            return '♣';
        case 3:
            return '♥';
        case 4:
            return '♠';
        default:
            return '';
    }
}

function isRed(card: Card): boolean {
    return (card.suit == 1 || card.suit == 3)
}

function flipCard() {
    emit("playAudio", "menuReturnSfx")
    isCardFlipped.value = !isCardFlipped.value
}
</script>
<template>
    <button class="poker-card-component" @click="flipCard">

        <Transition>
            <div class="card-face back" v-if=!isCardFlipped></div>

            <div class="card-face front" v-else-if=isCardFlipped>
                <div class=top-symbol>
                    <div :class="{ 'rank rank-top red': isRed(props.card), 'rank rank-top': isRed(props.card) == false }">
                        {{
                            props.card.rank }}</div>

                    <div
                        :class="{ 'minisuit suit-top red': isRed(props.card), 'minisuit suit-top': isRed(props.card) == false }">
                        {{ convertSymbol(props.card) }}</div>
                </div>

                <div :class="{ 'suit red': isRed(props.card), 'suit': isRed(props.card) == false }">{{
                    convertSymbol(props.card) }}</div>

                <div class=bottom-symbol>
                    <div
                        :class="{ 'minisuit suit-bottom red': isRed(props.card), 'minisuit suit-bottom': isRed(props.card) == false }">
                        {{ convertSymbol(props.card) }}</div>

                    <div
                        :class="{ 'rank rank-bottom red': isRed(props.card), 'rank rank-bottom': isRed(props.card) == false }">
                        {{ props.card.rank }}</div>
                </div>
            </div>
        </Transition>
    </button>
</template>
  
<style>
.v-enter-from {
    transform: rotateY(90deg)
}

.v-enter-active {
    transition: 0.25s linear 0.25s;
}

.v-leave-to {
    transform: rotateY(-90deg);
    transition: 0.25s linear;

}

.poker-card-component {
    width: 400px;
    height: 600px;
    border-radius: 10px;
    box-shadow: none;
    perspective: 1000px;
    background-color: transparent;

}

.poker-card-component:hover {
    cursor: grab;
    box-shadow: none;
}

.card-face {
    width: 100%;
    height: 100%;
    border-radius: 10px;
    background-repeat: no-repeat;
    background-size: cover;
    background-color: transparent;
    background-position: center;
}

.back {
    background-image: url("@/assets/images/cardRearBackground.png");
}

.front {
    display: grid;
    grid-template-rows: [top-symbol] auto [suit] auto [bottom-symbol] auto;
    background: url("@/assets/images/CardBackground.png");
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