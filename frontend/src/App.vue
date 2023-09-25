<script setup lang="ts">
import { RouterView } from 'vue-router'

import AudioController from '@/components/audioController/AudioController.vue';
import { AudioPlayer } from '@/composables/audioController/audioController'

let audio = new AudioPlayer()
</script>

<template>
  <AudioController 
    @toggle-mute="audio.toggleMuteAudio()">
  </AudioController>

  <RouterView
    @play-audio="audio.playAudio($event)"
    @stop-audio="audio.stopAudio()" 
  />
</template>

<style>
html,
body {
  margin: 0;
  height: 100%;
}
</style>
