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
    <main class="hilogame-main">
        <HiloGame @play-audio="$emit('playAudio', $event)"></HiloGame>
    </main>
</template>

<style scoped>
.hilogame-main {
    display: grid;
    place-items: center;
    min-height: 100vh;
    background-attachment: scroll;
    background-image: url("@/assets/images/GameScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>