<script lang="ts" setup>
import { Ref } from 'vue'

import MainMenu from '@/components/mainMenu/MainMenu.vue'
import AudioController from '@/components/audioController/AudioController.vue';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'toggleMuteAudio'): void
    (e: 'stopAudio'): void
}>()

interface Props {
    isMuted: Ref<boolean>
}

const props = defineProps<Props>()
</script>

<template>
  <main class="main-menu-main">
    <MainMenu @play-audio="$emit('playAudio', $event)"></MainMenu>
  </main>

  <footer class="main-menu-footer">
        <AudioController class="main-menu-audio-controller"
            @toggle-mute="$emit('toggleMuteAudio')"
            :isMuted="props.isMuted">
        </AudioController>
    </footer>
</template>

<style scoped>
.main-menu-main {
  background-image: url("@/assets/images/TableTexture.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.main-menu-audio-controller {
    position: absolute;
    bottom: 2vh;
    right: 2vw;
}
</style>