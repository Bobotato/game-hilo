<script lang="ts" setup>
import { ref, Ref } from 'vue'
import errorDialogue from '@/components/errorDialogue/errorDialogue.vue'
import { login } from '@/composables/auth/login'
import {
    APIServerDownError,
    InvalidCredentialsError
} from '@/services/apiService/errors'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

const { getCredentialsForm, tryLogin } = login()

let showPassword: Ref<boolean> = ref(false)

let isLoading: Ref<boolean> = ref(false)

let errorMessage: Ref<string> = ref("")

async function handleLogin() {
    try {
        emit("playAudio", "menuSelectSfx")
        isLoading.value = true
        errorMessage.value = ""
        const loginResponse = await tryLogin({ username: getCredentialsForm.value.username, password: getCredentialsForm.value.password })
        console.log(loginResponse)
    } catch (error: any) {
        switch (error.constructor) {
            case InvalidCredentialsError:
                errorMessage.value = 'The credentials provided were invalid. Please try again.'
                console.log(error.message)
                break
            case APIServerDownError:
                errorMessage.value = 'The auth server is down, please try again later.'
                console.log(error.message)
                break
            default:
                errorMessage.value = `Something went wrong, please try again later. The error is: ${error}`
                console.log(error.message)
                break
        }
    } finally {
        isLoading.value = false
    }
}

function togglePasswordShow() {
    showPassword.value = !showPassword.value
}
</script>

<template>
    <div class="login-menu">
        <div class="welcome-message">
            Welcome to Alex's hi-lo game.
            Please log-in or register.
        </div>

        <form class="login-fields" @submit.prevent="handleLogin">
            <input autofocus type="text" class="input username-input" placeholder="Username"
                v-model="getCredentialsForm.username" required>

            <div class="password-input-wrapper">
                <input v-if="showPassword" type="text" class="input password-input" v-model="getCredentialsForm.password"
                    placeholder="Password" required />
                <input v-else type="password" class="input password-input" v-model="getCredentialsForm.password"
                    placeholder="Password" required />

                <button
                    :class="{ 'toggle-password-button password-shown': showPassword, 'toggle-password-button password-hidden': !showPassword }"
                    @click="togglePasswordShow" type="button"></button>
            </div>

            <errorDialogue class="error_dialogue" v-if="errorMessage !== ''" :errorMessage="errorMessage">
            </errorDialogue>

            <button class="button login-button" type="submit" :disabled=isLoading>
                Log In
            </button>
        </form>

    </div>
</template>

<style scoped>
.login-menu {
    display: grid;
    border-radius: 10px;
    place-items: center;
    grid-template-rows: [welcome-message] auto [username-input] auto [password-input] auto [error-message] auto [login-button] auto [register-button] auto;
}

.welcome-message {
    grid-row: welcome-message;
    width: 50%;
    line-height: 150%;
    font-size: 1.5em;
    text-align: center;
    color: white;
    margin: 30px 20px;
}

.login-fields {
    display: grid;
    grid-template-rows: [username-input] auto [password-input] auto [error-message] auto [register-button] auto;
    place-items: center;
}

.input {
    height: 50px;
    border: none;
    outline: none;
    font-size: 1.5em;
    color: white;
    text-align: left;
    font-weight: 300;
    margin-bottom: 20px;
    padding: 0px 0px 0px 20px;
    background: rgba(3, 3, 3, 70%);
}

.input::placeholder {
    color: white;
}

.input:not(:focus):not(:placeholder-shown):invalid {
    border: 1px solid red;
}

.username-input {
    grid-row: username-input;
    width: 400px;
}

.password-input-wrapper {
    grid-row: password-input;
    display: grid;
    grid-template-columns: [password-input] 370px [password-view-toggle-button] 50px;
}

.password-input {
    margin-bottom: 20px;
}

input[type="password"] {
    font-size: 1em;
}

input[type="password"]::placeholder {
    font-size: 1.5em;
}

.toggle-password-button {
    height: 50px;
    width: 50px;
    background-color: rgba(3, 3, 3, 70%);
    background-repeat: no-repeat;
    background-size: 60%;
    background-position: center;
    border: none;
}

.password-shown {
    background-image: url('@/assets/icons/EyeSlashIcon.svg');
}

.password-hidden {
    background-image: url('@/assets/icons/EyeIcon.svg');
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

.login-button {
    grid-row: login-button;
    background-color: rgba(0, 48, 0, 80%);
}

.register-button {
    grid-row: register-button;
    background-color: rgba(48, 0, 0, 80%);
}
</style>@/composables/auth/authMenu@/composables/auth/login