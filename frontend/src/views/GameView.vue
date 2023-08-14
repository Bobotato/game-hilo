<script lang="ts" setup>
import loadingCover from '@/components/loading/loadingCover.vue'
import HiloGame from '@/components/game/HiloGame.vue';
</script>

<template>
    <div class="bg">
        <loadingCover v-if=false></loadingCover>
        <HiloGame></HiloGame>
    </div>
</template>

<style scoped>
.bg {
    background-image: url("@/assets/images/GameScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>