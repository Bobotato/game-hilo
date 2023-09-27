<script setup lang="ts">
import { onUnmounted } from 'vue';

import AuthMenu from '@/components/authMenu/AuthenticationMenu.vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'stopAudio'): void
}>()

setTimeout(function () {
    emit("playAudio", "menuThemeSfx")
}, 4000);


onUnmounted(() => {
    emit("stopAudio")
})
</script>

<template>
    <div class="authentication-main">
        <AuthMenu 
            @play-audio="$emit('playAudio', $event)">
        </AuthMenu>
    </div>
</template>

<style scoped>
.authentication-main {
    background-image: url("@/assets/images/loginScreen.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>