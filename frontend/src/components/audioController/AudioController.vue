<script lang="ts" setup>
import { ref, Ref } from 'vue'

const emit = defineEmits<{
    (e: 'toggleMute'): void
}>()

let isMuted: Ref<boolean> = ref(false)

function toggleMute() {
    isMuted.value = !isMuted.value
    console.log("Audio mute:", isMuted.value)
    emit('toggleMute')
}
</script>

<template>
    <div class=togglemute-main>
        <button :class="{ 'togglemute-button togglemute-button_audio-muted': isMuted, 'togglemute-button togglemute-button_audio-unmuted': !isMuted }"
            @click="toggleMute"></button>
    </div>
</template>

<style>
.togglemute-button {
    position: fixed;
    right: 1vw;
    bottom: 1vh;
    z-index: 999;
    width: 80px;
    height: 80px;
    background-color: rgba(255, 0, 0, 0);
    background-repeat: no-repeat;
    background-size: 60%;
    background-position: center;
}

.togglemute-button_audio-muted {
    background-image: url('@/assets/icons/Muted.svg');
}

.togglemute-button_audio-unmuted {
    background-image: url('@/assets/icons/Unmuted.svg');
}
</style>