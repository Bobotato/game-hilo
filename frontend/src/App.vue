<script setup lang="ts">
import { RouterView } from 'vue-router'
import { AudioPlayer } from '@/utils/audioController/audioController'

let audio = new AudioPlayer()

</script>

<template>
  <RouterView
    @play-audio="audio.playAudio($event)"
    @stop-audio="audio.stopAudio()"
    @toggle-mute-audio="audio.toggleMuteAudio()"
    :isMuted="audio.isMuted"/>
</template>

<style>
html,
body {
  margin: 0;
  height: 100%;
}
</style>