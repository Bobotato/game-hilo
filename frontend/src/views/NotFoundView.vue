<script lang="ts" setup>
import { router } from '@/router/index'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

function returnToMain() {
    router.push({ path: '/mainmenu' })
    emit('playAudio', 'menuSelectSfx')
}
</script>

<template>
    <main class="not-found-main">
        <div class="not-found-wrapper">
            <h2 class="not-found-message">There is nothing here. <br> Use this to go back to the front page.</h2>
            
            <button class="not-found-return-button"
                @click.once=returnToMain()>
                Back to Start
            </button>
        </div>
    </main>
</template>

<style scoped>
.not-found-main {
    height: 100vh;
    width: 100vw;
    background-image: url("@/assets/images/notFound.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    display: grid;
    place-items: center;
}

.not-found-wrapper {
    display: grid;
    grid-template-rows: [message] auto [button] auto;
    place-items: center;
}

.not-found-message {
    text-align: center;
    line-height: 2em;
}

.not-found-return-button {
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

.not-found-return-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

@media only screen and (max-width: 600px) {    
.not-found-message {
    line-height: 150%;
    font-size: 1.2em;
}

.not-found-return-button {
    width: 250px;
    font-size: 1.2em;
}
}
</style>