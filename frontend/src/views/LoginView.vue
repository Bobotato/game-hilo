<script setup lang="ts">
import { onMounted } from 'vue'
import AuthMenu from '@/components/auth/AuthMenu.vue'

// onMounted(() => {
//     menuThemeSfx()
// })
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
    background-image: url("@/assets/images/loginScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>