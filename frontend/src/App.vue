<script setup lang="ts">
import { RouterView } from 'vue-router'
import loadingCover from './components/loading/loadingCover.vue';

import AudioController from './components/audioPlayer/AudioController.vue';
import { AudioPlayer } from '@/services/soundPlayerService/SoundPlayerService'

let audio = new AudioPlayer()
</script>

<template>
  <header>
    <nav class="navigation_tabs">
      <RouterLink to="/">Pregame</RouterLink> |
      <RouterLink to="/mainmenu">Main Menu</RouterLink> |
      <RouterLink to="/game">Game</RouterLink> |
      <RouterLink to="/login">Login</RouterLink>
    </nav>
  </header>
  <AudioController @toggle-mute="audio.toggleMuteAudio()"></AudioController>
  <RouterView @play-audio="audio.playAudio($event)" @stop-audio="audio.stopAudio()" />
  <loadingCover class=loading-cover></loadingCover>
</template>

<style>
html,
body {
  margin: 0;
  height: 100%;
}

.navigation_tabs {
  background-color: green;
  color: white;
  display: flex;
  justify-content: center;
}

.loading-cover {
  position: absolute;
  left: 0;
  top: 0;
  z-index: -999
}
</style>
