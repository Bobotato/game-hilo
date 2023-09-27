<script lang="ts" setup>
import MainMenu from '@/components/mainMenu/MainMenu.vue'
</script>

<template>
  <div class="main-menu-main">
    <MainMenu @play-audio="$emit('playAudio', $event)"></MainMenu>
  </div>
</template>

<style scoped>
.main-menu-main {
  width: 100vw;
  height: 100vh;
  background-image: url("@/assets/images/TableTexture.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
</style>