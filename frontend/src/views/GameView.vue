<script lang="ts" setup>
import { onUnmounted, Ref } from 'vue';
import HiloGame from '@/components/game/HiloGame.vue';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'stopAudio'): void
    (e: 'toggleMuteAudio'): void
}>()

emit("playAudio", "gameThemeSfx")

interface Props {
    isMuted: Ref<boolean>
}

const props = defineProps<Props>()

onUnmounted(() => {
    emit("stopAudio")
})
</script>

<template>
    <main class="hilogame-main">
        <HiloGame @play-audio="$emit('playAudio', $event)"
                  @toggle-mute-audio="$emit('toggleMuteAudio')"
                  :isMuted="props.isMuted">
        </HiloGame>
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