<script lang="ts" setup>
import loadingCover from '@/components/loading/loadingCover.vue'
</script>

<template>
    <div class="bg">
        <loadingCover></loadingCover>
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