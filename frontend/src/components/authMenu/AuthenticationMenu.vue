<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import { router } from '@/router/index'

import LoginMenu from "@/components/authMenu/subcomponents/LoginMenu.vue"
import RegisterMenu from "@/components/authMenu/subcomponents/RegisterMenu.vue"

import { verifyJWT } from '@/services/apiService/user/user';

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'isLoading', enabled: string): void
}>()

let isShowingRegisterPage = ref(false)

async function checkIsLoggedIn() {
    try {
        await verifyJWT()
        router.push('/mainmenu')
    } catch (error: any) {
        return
    }
}

function toggleShowRegisterPage() {
    emit("playAudio", "menuReturnSfx")
    isShowingRegisterPage.value = !isShowingRegisterPage.value
}

onMounted (() => {
    checkIsLoggedIn()
})
</script>

<template>
    <div class="auth-menu-main">
        <div class="auth-menu-wrapper">
            <RegisterMenu
                v-if="isShowingRegisterPage"
                @play-audio="$emit('playAudio', $event)">
            </RegisterMenu>

            <LoginMenu
                v-else
                @play-audio="$emit('playAudio', $event)">
            </LoginMenu>

            <button class="auth-menu-button auth-menu-button_switch-to-login"
                v-if="isShowingRegisterPage"
                @click="toggleShowRegisterPage">
                Login Page
            </button>

            <button class="auth-menu-button auth-menu-button_switch-to-register"
                v-else
                @click="toggleShowRegisterPage">
                Register Page
            </button>

        </div>
    </div>
</template>

<style scoped>
.auth-menu-main {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.auth-menu-wrapper {
    display: grid;
    grid-template-rows: [auth-menu] auto [toggle-button] auto;
    justify-items: center;
}

.auth-menu-button {
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

.auth-menu-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

.auth-menu-button_switch-to-register {
    grid-row: toggle-button;
    background-color: rgba(48, 0, 0);
}

.auth-menu-button_switch-to-login {
    grid-row: toggle-button;
    background-color: rgba(0, 48, 0);
}

@media only screen and (max-width: 600px) {    
.auth-menu-button {
    font-size: 1.2em;
}
}
</style>