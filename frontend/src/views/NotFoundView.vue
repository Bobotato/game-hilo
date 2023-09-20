<script lang="ts" setup>
import { router } from '@/router/index'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

function returnToMain() {
    router.push({ path: '/' })
    emit('playAudio', 'menuSelectSfx')
}
</script>

<template>
    <div class="bg">
        <div class="component">
            <h2 class="message">There is nothing here. <br> Use this to go back to the front page.</h2>
            <button class="return-button" @click.once=returnToMain()>Back to Start</button>
        </div>
    </div>
</template>

<style scoped>
.bg {
    background-image: url("@/assets/images/notFound.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;

    width: 100vw;
    display: grid;
    place-items: center;
}

.component {
    display: grid;
    grid-template-rows: [message] auto [button] auto;
    place-items: center;
}

.message {
    text-align: center;
    line-height: 2em;
}

.return-button {
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

.return-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}
</style>