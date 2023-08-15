<script lang="ts">
export default {
    props: {
        rank: String,
        suit: String
    },
    computed: {
        suitSymbol() {
            switch (this.suit) {
                case 'hearts':
                    return '♥';
                case 'diamonds':
                    return '♦';
                case 'clubs':
                    return '♣';
                case 'spades':
                    return '♠';
                default:
                    return '';
            }
        },
        isRed() {
            return this.suit === 'hearts' || this.suit === 'diamonds';
        }
    }
};
</script>

<template>
    <div class="card" :class="[suit, { 'red': isRed }]">
        <div class="rank">{{ rank }}</div>
        <div class="suit">{{ suitSymbol }}</div>
    </div>
</template>
  
<style scoped>
.card {
    width: 200px;
    height: 300px;
    background: url("@/assets/images/CardBackground.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px;
    font-size: 24px;
    font-weight: bold;
    box-shadow: rgba(0, 0, 0, 0.55) 0px 3px 8px;
}

.red {
    color: red;
}
</style>