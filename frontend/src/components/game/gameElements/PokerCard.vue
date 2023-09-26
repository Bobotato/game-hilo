<script lang="ts" setup>
import { ref } from 'vue'
import { Card } from '@/types/gameElements/gameElementTypes';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

interface Props {
    card: Card
    isStatic: boolean
}

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

function convertNumeric(card: Card): string {
    switch (card.rank) {
        case 1:
            return 'A';
        case 2:
            return '2';
        case 3:
            return '3';
        case 4:
            return '4';
        case 5:
            return '5';
        case 6:
            return '6';
        case 7:
            return '7';
        case 8:
            return '8';
        case 9:
            return '9';
        case 10:
            return '10';
        case 11:
            return 'J';
        case 12:
            return 'Q';
        case 13:
            return 'K';
        default:
            return '';
    }
}

function isRed(card: Card): boolean {
    return (card.suit == 1 || card.suit == 3)
}

function flipCard() {
    if (!props.isStatic) {
        emit("playAudio", "menuReturnSfx")
        isCardFlipped.value = !isCardFlipped.value
    }
}

let isCardFlipped = ref(false)

if (props.isStatic) {
    isCardFlipped.value = true
}
</script>
<template>
    <button class="card-main" @click="flipCard">

        <Transition>
            <div class="card-face card-face_back" v-if="!isCardFlipped && !isStatic"></div>

            <div class="card-face card-face_front" v-else-if="isCardFlipped || isStatic">
                <div class=card-top-symbols>
                    <div :class="{ 'rank rank-top red': isRed(props.card), 'rank rank-top': isRed(props.card) == false }">
                        {{
                            convertNumeric(props.card) }}</div>

                    <div
                        :class="{ 'minisuit suit-top red': isRed(props.card), 'minisuit suit-top': isRed(props.card) == false }">
                        {{ convertSymbol(props.card) }}</div>
                </div>

                <div :class="{ 'suit red': isRed(props.card), 'suit': isRed(props.card) == false }">{{
                    convertSymbol(props.card) }}</div>

                <div class=card-bottom-symbols>
                    <div
                        :class="{ 'minisuit suit-bottom red': isRed(props.card), 'minisuit suit-bottom': isRed(props.card) == false }">
                        {{ convertSymbol(props.card) }}</div>

                    <div
                        :class="{ 'rank rank-bottom red': isRed(props.card), 'rank rank-bottom': isRed(props.card) == false }">
                        {{ convertNumeric(props.card) }}</div>
                </div>
            </div>
        </Transition>
    </button>
</template>
  
<style scoped>
.v-enter-from {
    opacity: 0%;
    transform: rotateY(90deg)
}

.v-enter-active {
    transition-property: transform, opacity;
    transition-delay: 0.4s;
    transition-duration: 0.2s, 1ms;
}

.v-enter-to {
    opacity: 100%;
}

.v-leave-from {
    opacity: 100%;
}

.v-leave-active {
    transition-property: transform, opacity;
    transition-delay: 0s, 0.2s;
    transition-duration: 0.2s, 1ms;
}

.v-leave-to {
    transform: rotateY(-90deg);
    opacity: 0%;
}

.card-main {
    width: 100%;
    height: 100%;
    box-shadow: none;
    perspective: 1000px;
    background-color: transparent;
}

.card-main:hover {
    cursor: grab;
    box-shadow: none;
}

.card-face {
    width: 100%;
    height: 100%;
    border-radius: 20px;
}

.card-face_back {
    background: url("@/assets/images/cardRearBackground.png");
    background-position: center;
    background-size: 100% 102%;
}

.card-face_front {
    background: url("@/assets/images/CardBackground.png");
    display: grid;
    grid-template-rows: [card-top-symbols] 25% [suit] 50% [card-bottom-symbols] 25%;
    background-position: center;
    background-repeat: no-repeat;
}

.rank {
    font-size: 40px;
    font-weight: bold;
    letter-spacing: -5px;
}

.minisuit {
    font-size: 70px;
    font-weight: bold;
    letter-spacing: -5px;
}

.card-top-symbols {
    display: grid;
    align-self: start;
    place-items: center;
    grid-template-rows: [rank-top] 50px [suit-top] 60px;
    margin: 20px 0 0 10px;
    justify-self: start;
}

.suit-top {
    grid-row: suit-top;
}

.rank-top {
    grid-row: rank-top;
}

.card-bottom-symbols {
    display: grid;
    place-items: center;
    grid-template-rows: [rank-bottom] 50px [suit-bottom] 60px;
    transform: rotate(180deg);
    margin: 0 10px 20px 0;
    justify-self: end;
}

.suit-bottom {
    grid-row: suit-bottom;
}

.rank-bottom {
    grid-row: rank-bottom;
}

.suit {
    grid-row: suit;
    line-height: 265px;
    font-size: 200px;
    text-align: center;
}

.red {
    color: rgb(139, 0, 0);
}
</style>