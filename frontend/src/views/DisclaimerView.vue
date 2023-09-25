<script lang="ts" setup>
import { onUnmounted } from 'vue';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let descriptionText = "This game might be slightly spooky, with spooky sounds and dismembered bits. \n Use the mute icon on the bottom right to disable sounds."

onUnmounted(() => {
    emit('playAudio', 'enterConfirmSfx')
})
</script>

<template>
    <div class="disclaimer-component">
        <div class="description-wrapper">
            <h2 class="description-text">{{ descriptionText }}</h2>

            <RouterLink to="/login">
                <button class="description-continue-button"
                    @click="emit('playAudio', 'menuSelectSfx')">
                    Continue
                </button>
            </RouterLink>
        </div>
    </div>
</template>

<style scoped>
.disclaimer-component {
    display: flex;
    height: 100vh;
    justify-content: center;
    align-items: center;
    background-color: black;
}

.description-wrapper {
    display: grid;
    justify-items: center;
    align-items: center;
    text-align: center;
    grid-template-rows: [description-text] auto [continue-button] auto;
}

.description-text {
    line-height: 200%;
    font-size: 1.5em;
    white-space: pre-wrap;
    text-align: center;
    color: white;
}

.description-continue-button {
    height: 50px;
    width: 300px;
    border: none;
    border-radius: 10px;
    padding: 10px;
    margin: 20px 0px 20px 0px;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
    background-color: rgba(48, 0, 0);
}

.description-continue-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}
</style>