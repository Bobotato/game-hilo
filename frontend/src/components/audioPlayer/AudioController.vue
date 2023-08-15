<script lang="ts" setup>
import { ref } from 'vue'
import { AudioPlayer } from '@/services/soundPlayerService/SoundPlayerService'

let audio = ref(new AudioPlayer("", 0.1))
</script>

<template>
    <div class="mute-button">
        <button
            :class="{ 'toggle-mute-button audio-muted': audio.isMuted, 'toggle-mute-button audio-unmuted': !audio.isMuted }"
            @click="audio.toggleMuteAudio"></button>
    </div>
</template>

<style>
.toggle-mute-button {
    position: absolute;
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

.audio-muted {
    background-image: url('@/assets/icons/Muted.svg');
}

.audio-unmuted {
    background-image: url('@/assets/icons/Unmuted.svg');
}
</style>