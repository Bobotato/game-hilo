<script lang="ts" setup>
import { ref } from 'vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

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
    <div class="main-menu-main">
        <div class="main-menu">
            <h2 class="main-menu-message" v-if="!ruleSet.isShowing">Welcome to the table.</h2>
            <h2 class="main-menu-ruleset" v-if="ruleSet.isShowing">{{ ruleSet.text }}</h2>

            <RouterLink to="/game">
                <div class="main-menu-button-wrapper">
                    <button class="main-menu-button main-menu-button_play-button"
                        @click="emit('playAudio', 'menuSelectSfx')">
                        Play
                    </button>
                </div>
            </RouterLink>

            <div class="main-menu-button-wrapper">
                <button class="main-menu-button main-menu-button_ruleset-button"
                    @click="showRuleset">
                    Ruleset
                </button>
            </div>

            <div class="main-menu-button-wrapper">
                <RouterLink to="/login">
                    <button class="main-menu-button main-menu-button_leave-button"
                        @click="emit('playAudio', 'menuReturnSfx')">
                        Leave
                    </button>
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

.main-menu-main {
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
    grid-template-rows: [main-menu-message] auto [main-menu-button_play-button] auto [main-menu-button_ruleset-button] auto [main-menu-button_leave-button] auto;
}

.main-menu-message {
    grid-row: main-menu-message;
}

.main-menu-button-wrapper {
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
    background-color: rgba(48, 0, 0);
}

.main-menu-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

.main-menu-button_play-button {
    grid-row: main-menu-button_play-button;
}

.main-menu-button_ruleset-button {
    grid-row: main-menu-button_ruleset-button;
}

.main-menu-button_leave-button {
    grid-row: main-menu-button_leave-button;
}
</style>