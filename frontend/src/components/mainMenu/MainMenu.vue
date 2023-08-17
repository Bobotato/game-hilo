<script lang="ts" setup>
import { ref } from 'vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let playerName = ref("stranger")

let ruleSet = ref({
    isShowing: false,
    text: 'The game uses a standard 52 card deck. \n\n 1 card is dealt face up, and another face down. \n\n You need to guess if the face down card is of a higher or lower value than the face up card. \n\n A right answer doubles your bet, and a wrong answer forfeits your bet. Happy playing.'
})

function showRuleset() {
    emit("playAudio", "menuSelectSfx")
    ruleSet.value.isShowing = !ruleSet.value.isShowing
}
</script>

<template>
    <div class="main-menu-component">
        <div class="main-menu">
            <h2 class="welcome-message" v-if="!ruleSet.isShowing">Welcome to the table, {{ playerName }}.</h2>
            <h2 class="ruleset" v-if="ruleSet.isShowing">{{ ruleSet.text }}</h2>

            <RouterLink to="/game">
                <div class="button-wrapper">
                    <button class="main-menu-button play-button">Play</button>
                </div>
            </RouterLink>

            <div class="button-wrapper">
                <button class="main-menu-button ruleset-button" @click="showRuleset">Ruleset</button>
            </div>

            <div class="button-wrapper">
                <RouterLink to="/login">
                    <button class="main-menu-button leave-button">Leave</button>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<style scoped>
h2 {
    white-space: pre-wrap;
    text-align: center;
    color: white;
}

.main-menu-component {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.main-menu {
    display: grid;
    width: 500px;
    align-items: center;
    justify-content: center;
    grid-template-rows: [welcome-message] auto [play-button] auto [ruleset-button] auto [leave-button] auto;
}

.welcome-message {
    grid-row: welcome-message;
}

.button-wrapper {
    display: flex;
    justify-content: center;
}

.main-menu-button {
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
    background-color: rgba(48, 0, 0, 80%);
}

.main-menu-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

.play-button {
    grid-row: play-button;
}

.ruleset-button {
    grid-row: ruleset-button;
}

.leave-button {
    grid-row: leave-button;
}
</style>