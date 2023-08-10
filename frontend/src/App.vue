<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="navigation_tabs">
        <RouterLink to="/mainmenu">Main Menu</RouterLink>
        <RouterLink to="/game">Game</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<style>
html, body {
  margin:0;
  height:100%;
}

.navigation_tabs {
  background-color: green;
  color: white;
  display: flex;
  justify-content: center;
}
</style>
