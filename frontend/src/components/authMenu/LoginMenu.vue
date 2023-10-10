<script lang="ts" setup>
import { ref, Ref } from 'vue'
import { router } from '@/router/index'

import ErrorWarning from '@/components/errorWarning/ErrorWarning.vue'
import LoadingPage from '@/components/loading/LoadingPage.vue'

import { useAuthComposable } from '@/composables/authMenu/auth'
import {
    APIServerDownError,
    InvalidCredentialsError
} from '@/services/apiService/errors'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

const { getCredentialsForm, loginAccount } = useAuthComposable()

let showPassword: Ref<boolean> = ref(false)

let isLoading: Ref<boolean> = ref(false)

let errorString: Ref<string> = ref("")

async function handleLogin() {
    try {
        emit("playAudio", "menuSelectSfx")
        
        isLoading.value = true
        errorString.value = ""

        const loginResponse = await loginAccount(getCredentialsForm.value)
        console.log(loginResponse)

        router.push({ path: '/mainmenu' })
    } catch (error: any) {
        switch (error.constructor) {
            case InvalidCredentialsError:
                errorString.value = 'The credentials provided were invalid. Please try again.'
                console.log(error.message)
                break
            case APIServerDownError:
                errorString.value = 'The auth server is down, please try again later.'
                console.log(error.message)
                break
            default:
                errorString.value = `Something went wrong, please try again later. The error is: ${error}`
                console.log(error.message)
                break
        }
    } finally {
        isLoading.value = false
    }
}

function toggleShowPassword() {
    showPassword.value = !showPassword.value
}
</script>

<template>
    <LoadingPage v-if=isLoading></LoadingPage>

    <main class="login-menu-main">
        <div class="login-instructions">
            Welcome to Alex's hi-lo game. <br>
            Please log-in or register.
        </div>

        <form class="login-form" @submit.prevent="handleLogin">

            <input class="login-form-input login-form-input_username-input" 
                autofocus type="text"
                placeholder="Username"
                v-model="getCredentialsForm.username"
                required
            >

            <div class="login-form-input_password-input-wrapper">
                
                <input class="login-form-input login-form-input_password-input"
                    v-if="showPassword"
                    type="text"
                    v-model="getCredentialsForm.password"
                    placeholder="Password"
                    required
                />

                <input class="login-form-input login-form-input_password-input"
                    v-else
                    type="password" 
                    v-model="getCredentialsForm.password"
                    placeholder="Password"
                    required
                />

                <button
                    :class="{ 'toggle-password-button toggle-password-button_password-shown': showPassword, 'toggle-password-button toggle-password-button_password-hidden': !showPassword }"
                    @click="toggleShowPassword"
                    type="button"></button>
            </div>

            <ErrorWarning class="error-warning"
                v-if="errorString !== ''"
                :errorString="errorString">
            </ErrorWarning>

            <button class="login-submit-button"
                type="submit"
                :disabled=isLoading>
                Log In
            </button>
        </form>
    </main>
</template>

<style scoped>
.login-menu-main {
    display: grid;
    border-radius: 10px;
    place-items: center;
    grid-template-rows: [login-instructions] auto [username-input] auto [password-input] auto [error-message] auto [login-button] auto [register-button] auto;
}

.login-instructions {
    grid-row: login-instructions;
    width: 90%;
    line-height: 150%;
    font-size: 1.5em;
    text-align: center;
    color: white;
    margin: 30px 20px;
}

.login-form {
    display: grid;
    grid-template-rows: [username-input] auto [password-input] auto [error-message] auto [register-button] auto;
    place-items: center;
}

.login-form-input {
    height: 50px;
    border: none;
    outline: none;
    font-size: 1.5em;
    color: white;
    text-align: left;
    font-weight: 300;
    margin: 0 0 20px 0;
    padding: 0px 0px 0px 20px;
    background: rgba(3, 3, 3);
    border: 1px solid white;
}

.login-form-input::placeholder {
    color: white;
}

.login-form-input:not(:focus):not(:placeholder-shown):invalid {
    border: 1px solid red;
}

.login-form-input_username-input {
    grid-row: username-input;
    width: 400px;
}

.login-form-input_password-input-wrapper {
    grid-row: password-input;
    display: grid;
    grid-template-columns: [password-input] 370px [password-view-toggle-button] 50px;
}

.login-form-input_password-input {
    margin: 0 0 20px 0;
    border-style: solid none solid solid;
}

input[type="password"]::placeholder {
    font-size: 1em;
}

.toggle-password-button {
    height: 52px;
    width: 50px;
    padding: 0px;
    background-color: rgba(3, 3, 3);
    background-repeat: no-repeat;
    background-size: 60%;
    background-position: center;
    border: 1px solid rgb(255, 255, 255);
    border-style: solid solid solid none;
}

.toggle-password-button:active {
    transform: none;
}

.toggle-password-button_password-shown {
    background-image: url('@/assets/icons/EyeSlashIcon.svg');
}

.toggle-password-button_password-hidden {
    background-image: url('@/assets/icons/EyeIcon.svg');
}

.login-submit-button {
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
    grid-row: login-button;
    background-color: rgba(0, 48, 0);
}

.login-submit-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

@media only screen and (max-width: 600px) {    
.login-instructions {
    line-height: 150%;
    font-size: 1.2em;
}

.login-form-input {
    font-size: 1.2em;
}

.login-form-input::placeholder {
    font-size: 1em;
}


.login-form-input_username-input {
    width: 300px;
}

.login-form-input_password-input-wrapper {
    grid-template-columns: [password-input] 270px [password-view-toggle-button] 50px;
}

.login-submit-button {
    font-size: 1.2em;
}
}
</style>