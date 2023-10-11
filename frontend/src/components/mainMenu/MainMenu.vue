<script lang="ts" setup>
import { ref } from 'vue'
import { AxiosError } from 'axios';

import ErrorOverlay from '../errorWarning/ErrorOverlay.vue';

import { APIServerDownError, UnauthorisedError } from '@/services/apiService/errors';

import { logOut } from '@/utils/logOut'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

let ruleSet = ref({
    isShowing: false,
    text: 'A card is dealt face-up. \n\n You must predict if the next card will be higher or lower.'
})

let errorOverlay = ref({
    errorString: "",
    isShowing: false
})

function showRuleset() {
    emit("playAudio", "menuSelectSfx")
    ruleSet.value.isShowing = !ruleSet.value.isShowing
}

function logOutFromMainMenu() {
    emit('playAudio', 'menuSelectSfx')
    try {
        logOut()
        
    } catch (error: any) {
        switch (error.constructor) {
            case UnauthorisedError:
                errorOverlay.value.errorString = 'There is an issue with the login token. Please login again.'
                errorOverlay.value.isShowing = true
                break
            case APIServerDownError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                errorOverlay.value.isShowing = true
                break
            case AxiosError:
                errorOverlay.value.errorString = 'There is an issue with the game server. Please try again later.'
                errorOverlay.value.isShowing = true
                break
    }
}
}
</script>

<template>
    <main class="main-menu-main">
        <ErrorOverlay 
            v-if="errorOverlay.isShowing"
            :errorString=errorOverlay.errorString
            @play-audio="$emit('playAudio', $event)">
        </ErrorOverlay>

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
                <button class="main-menu-button main-menu-button_leave-button"
                    @click.once="logOutFromMainMenu">
                    Log Out
                </button>
            </div>
        </div>
    </main>
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

@media only screen and (max-width: 600px) {
.main-menu-message {
    font-size: 1.2em;
}

.main-menu-ruleset {
    margin: 10px 30px;
    font-size: 1.2em;
}

.main-menu-button {
    font-size: 1.2em;
}
} 
</style>