<script setup lang="ts">
import { onUnmounted, Ref } from 'vue';

import AudioController from '@/components/audioController/AudioController.vue';
import AuthMenu from '@/components/authMenu/AuthenticationMenu.vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'stopAudio'): void
    (e: 'toggleMuteAudio'): void
}>()

interface Props {
    isMuted: Ref<boolean>
}

const props = defineProps<Props>()

setTimeout(function () {
    emit("playAudio", "menuThemeSfx")
}, 4000);


onUnmounted(() => {
    emit("stopAudio")
})
</script>

<template>
    <main class="authentication-main">
        <AuthMenu 
            @play-audio="$emit('playAudio', $event)">
        </AuthMenu>

        <AudioController class="authentication-audio-controller"
            @toggle-mute="$emit('toggleMuteAudio')"
            :isMuted="props.isMuted">
        </AudioController>
    </main>
</template>

<style scoped>
.authentication-main {
    background-image: url("@/assets/images/loginScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}

.authentication-audio-controller {
    position: absolute;
    bottom: 2vh;
    right: 2vw;
}
</style>