<script lang="ts" setup>
import { ref } from 'vue'

import LoginMenu from "@/components/auth/authElements/LoginMenu.vue"
import RegisterMenu from "@/components/auth/authElements/RegisterMenu.vue"

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'isLoading', enabled: string): void
}>()

let isShowingRegisterPage = ref(false)

function toggleRegister() {
    emit("playAudio", "menuReturnSfx")
    isShowingRegisterPage.value = !isShowingRegisterPage.value
}
</script>

<template>
    <div class="auth-component">
        <div class="auth-menu">
            <RegisterMenu v-if="isShowingRegisterPage" @play-audio="$emit('playAudio', $event)"></RegisterMenu>
            <button class="button goto-register-button" v-if="!isShowingRegisterPage" @click="toggleRegister">
                Register
            </button>

            <LoginMenu v-if="!isShowingRegisterPage" @play-audio="$emit('playAudio', $event)"></LoginMenu>
            <button class="button goto-login-button" v-if="isShowingRegisterPage" @click="toggleRegister">
                Back to Login
            </button>

        </div>
    </div>
</template>

<style scoped>
.auth-component {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.auth-menu {
    display: grid;
    width: 800px;
    grid-template-rows: [auth-menu] auto [toggle-button] auto;
    justify-items: center;
}

.button {
    height: 50px;
    width: 250px;
    border: none;
    border-radius: 10px;
    padding: 10px;
    margin: 20px 10px 10px 10px;
    text-align: center;
    line-height: 1.5;
    font-size: 1.5em;
    color: white;
    box-shadow: 3px 3px 5px black;
}

.button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

.goto-register-button {
    grid-row: toggle-button;
    background-color: rgba(48, 0, 0);
}

.goto-login-button {
    grid-row: toggle-button;
    background-color: rgba(0, 48, 0);
}
</style>