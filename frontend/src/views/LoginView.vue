<script setup lang="ts">
import { onUnmounted } from 'vue';
import AuthMenu from '@/components/auth/AuthMenu.vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'stopAudio'): void
}>()

setTimeout(function () {
    emit("playAudio", "menuThemeSfx")
}, 5000);


onUnmounted(() => {
    console.log("Component unmounted")
    emit("stopAudio")
})
</script>

<template>
    <div class="bg">
        <AuthMenu @play-audio="$emit('playAudio', $event)"></AuthMenu>
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