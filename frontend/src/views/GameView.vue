<script lang="ts" setup>
import loadingCover from '@/components/loading/loadingCover.vue'
import ReceiveItem from '@/components/game/ReceiveItem.vue'
</script>

<template>
    <div class="bg">
        <loadingCover v-if=false></loadingCover>
        <ReceiveItem :itemName="`tester`" :item-quantity=1 :item-image-source="`../../assets/images/Fingers.png`">
        </ReceiveItem>
    </div>
</template>

<style scoped>
.bg {
    width: 100vw;
    height: 100vh;
    background-image: url("@/assets/images/GameScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>