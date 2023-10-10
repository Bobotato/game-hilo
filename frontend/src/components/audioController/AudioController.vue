<script lang="ts" setup>
import { ref, Ref } from 'vue'

const emit = defineEmits<{
    (e: 'toggleMute'): void
}>()

interface Props {
    isMuted: Ref<boolean>
}

const props = defineProps<Props>()

let isAudioMuted: Ref<boolean> = ref(false)

if (props.isMuted.value) {
    isAudioMuted.value = true
}

function toggleMute() {
    isAudioMuted.value = !isAudioMuted.value
    emit('toggleMute')
}
</script>

<template>
    <main class=togglemute-main>
        <button :class="{ 'togglemute-button togglemute-button_audio-muted': isAudioMuted, 'togglemute-button togglemute-button_audio-unmuted': !isAudioMuted }"
            @click="toggleMute">
        </button>
    </main>
</template>

<style scoped>
.togglemute-button {
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