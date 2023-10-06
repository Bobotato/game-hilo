<script lang="ts" setup>
import { onUnmounted } from 'vue';
import HiloGame from '@/components/game/HiloGame.vue';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'stopAudio'): void
}>()

emit("playAudio", "gameThemeSfx")

onUnmounted(() => {
    emit("stopAudio")
})
</script>

<template>
    <div class="game-main">
        <HiloGame @play-audio="$emit('playAudio', $event)"></HiloGame>
    </div>
</template>

<style scoped>
.game-main {
    background-image: url("@/assets/images/GameScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>