<script lang="ts" setup>
import AuthMenu from '@/components/auth/AuthMenu.vue'
</script>

<template>
  <div class="bg">
    <AuthMenu></AuthMenu>
  </div>
</template>

<style scoped>
.bg {
  width: 100vw;
  height: 100vh;
  background-image: url("@/assets/images/TableTexture.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
</style>