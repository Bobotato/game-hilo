<script lang="ts" setup>
import { ref, Ref } from 'vue'
let isMuted: Ref<boolean> = ref(false)

const emit = defineEmits(['toggleMute'])

function toggleMute() {
    isMuted.value = !isMuted.value
    console.log(isMuted.value)
    emit('toggleMute')
}
</script>

<template>
    <div class="mute-button">
        <button :class="{ 'toggle-mute-button audio-muted': isMuted, 'toggle-mute-button audio-unmuted': !isMuted }"
            @click="toggleMute"></button>
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