<script lang="ts" setup>
import { ref } from 'vue'
import { Card } from '@/types/gameElements/gameElementTypes';
import { CardRanks } from '@/services/card';

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
                            CardRanks[props.card.rank] }}</div>

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
                        {{ CardRanks[props.card.rank] }}</div>
                </div>
            </div>
        </Transition>
    </button>
</template>
  
<style scoped>
.v-enter-from {
    transform: rotateY(90deg)
}

.v-enter-active {
    transition: 0.2s linear 0.2s;
}

.v-leave-to {
    transform: rotateY(-90deg);
    transition: 0.2s linear;

}

.poker-card-component {
    width: 100%;
    height: 100%;
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
    border-radius: 20px;
}

.back {
    background: url("@/assets/images/cardRearBackground.png");
    background-position: center;
    background-size: 100% 102%;
}

.front {
    background: url("@/assets/images/CardBackground.png");
    display: grid;
    grid-template-rows: [top-symbol] 25% [suit] 50% [bottom-symbol] 25%;
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

.top-symbol {
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

.bottom-symbol {
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