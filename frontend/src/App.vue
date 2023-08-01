<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="navigation_tabs">
        <RouterLink to="/main_menu">Main Menu</RouterLink>
        <RouterLink to="/game">Game</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
.navigation_tabs {
  background-color: green;
  color: white;
  display: flex;
  justify-content: center;
}
</style>
