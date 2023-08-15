<script setup lang="ts">
import { onMounted } from 'vue'
import AuthMenu from '@/components/auth/AuthMenu.vue'

import { AudioPlayer } from '@/services/soundPlayerService/SoundPlayerService'

let audio = new AudioPlayer("", 0.1)

onMounted(() => {
    audio.menuThemeSfx()
})
</script>

<template>
    <div class="bg">
        <AuthMenu></AuthMenu>
    </div>
</template>

<style scoped>
.bg {
    background-image: url("@/assets/images/loginScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>