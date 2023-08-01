<script setup lang="ts">
import LoginMenu from "@/components/LoginMenu.vue"
</script>

<template>
    <div class="bg">
        <LoginMenu></LoginMenu>
    </div>
</template>

<style>
body {
    width: 100vw;
    height: 100vh;
    background-image: url("../assets/images/loginScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }
</style>