<script lang="ts" setup>
import { router } from '@/router/index'

interface Props {
    errorString: string
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

function returnToLogin() {
    emit('playAudio', 'menuSelectSfx')
    router.push({ path: '/login' })
}
</script>

<template>
    <div class="error-overlay-component" v-if="props.errorString != ''">
        <div class="error-overlay-wrapper">
            <img class="error-icon" src="@/assets/images/errorIcon.svg">
            <h2 class="error-message">An error has occured: <br> {{ props.errorString }}</h2>
            <button class="return-to-login-button" @click.once="returnToLogin">Return to Login</button>
        </div>
    </div>
</template>

<style scoped>
.error-overlay-component {
    backdrop-filter: blur(10px) grayscale(50%);
    background-color: rgba(0, 0, 0, 0.5);
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 1000;
    display: grid;
    place-items: center;
}

.error-overlay-wrapper {
    display: grid;
    grid-template-rows: [icon] auto [message] auto [button] auto;
    gap: 30px;
    place-items: center;
}

.error-icon {
    grid-row: icon;
    width: 50px;
    height: 50px;
}

.error-message {
    grid-row: message;
    text-align: center;
    font-size: 1.5em;
    line-height: 2em;
}

.return-to-login-button {
    height: 50px;
    width: 250px;
    border: none;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
    background-color: rgba(48, 0, 0);
}

.button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    cursor: pointer;
}

.button:active {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
    transform: translateY(4px);
}

@media only screen and (max-width: 600px) {
  .error-message {
    font-size: 1.2em;
  }
  .return-to-login-button {
    font-size: 1.2em;
  }
}
</style>