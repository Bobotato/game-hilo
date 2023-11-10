<script lang="ts" setup>
import { ref, Ref } from 'vue'
import { router } from '@/router/index'

import ErrorWarning from '@/components/errorWarning/ErrorWarning.vue'
import LoadingPage from '@/components/loading/LoadingPage.vue';

import { useAuthComposable } from '@/composables/authMenu/auth';
import {
    APIServerDownError,
    UsernameAlreadyExistsError
} from '@/services/apiService/errors'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
}>()

const { getCredentialsForm, registerAccount } = useAuthComposable()

let showPassword: Ref<boolean> = ref(false)

let isLoading: Ref<boolean> = ref(false)

let errorString: Ref<string> = ref("")

async function handleRegister() {
    try {
        emit("playAudio", "menuSelectSfx")

        isLoading.value = true
        errorString.value = ""

        await registerAccount(getCredentialsForm.value)

        router.push({ path: '/mainmenu' })

    } catch (error: any) {
        switch (error.constructor) {
            case UsernameAlreadyExistsError:
                errorString.value = 'There is already a user with this username. Please try again.'
                break
            case APIServerDownError:
                errorString.value = 'The auth server is down, please try again later.'
                break
            default:
                errorString.value = `Something went wrong, please try again later. The error is: ${error}`
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
    
    <main class="register-menu-main">
        <div class="register-instructions">
            Please register your details.
        </div>

        <form class="register-form" @submit.prevent="handleRegister">

            <input class="register-form-input register-form-input_username-input" 
                autofocus
                type="text"
                placeholder="Username"
                v-model="getCredentialsForm.username"
                required
            />

            <div class="register-form-input_password-input-wrapper">
                <input class="register-form-input register-form-input_password-input"
                    v-if="showPassword"
                    type="text"
                    v-model="getCredentialsForm.password"
                    placeholder="Password" 
                    required 
                />

                <input class="register-form-input register-form-input_password-input" 
                    v-else 
                    type="password"  
                    v-model="getCredentialsForm.password"
                    placeholder="Password"
                    required 
                />

                <button
                    :class="{ 'toggle-password-button toggle-password-button_password-shown': showPassword, 'toggle-password-button toggle-password-button_password-hidden': !showPassword }"
                    @click="toggleShowPassword"
                    type="button">
                </button>
            </div>

            <ErrorWarning class="error-warning"
                v-if="errorString !== ''" 
                :errorString="errorString">
            </ErrorWarning>

            <button class="register-submit-button" 
                type="submit" 
                :disabled=isLoading>
                Register
            </button>
        </form>
    </main>
</template>

<style scoped>
.register-menu-main {
    display: grid;
    border-radius: 10px;
    place-items: center;
    grid-template-rows: [register-instructions] auto [register-form] auto;
}

.register-instructions {
    grid-row: register-instructions;
    width: 50%;
    line-height: 150%;
    font-size: 1.5em;
    text-align: center;
    color: white;
    margin: 30px 20px;
}

.register-form {
    display: grid;
    grid-template-rows: [username-input] auto [password-input] auto [error-message] auto [register-button] auto;
    place-items: center;
}

.register-form-input {
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

.register-form-input::placeholder {
    color: white;
}

.register-form-input:not(:focus):not(:placeholder-shown):invalid {
    border: 1px solid red;
}

.register-form-input_username-input {
    grid-row: username-input;
    width: 400px;
}

.register-form-input_password-input-wrapper {
    grid-row: password-input;
    display: grid;
    grid-template-columns: [password-input] 370px [password-view-toggle-button] 50px;
}

.register-form-input_password-input {
    margin: 0 0 20px 0;
    border-style: solid none solid solid;
}

input[type="password"]::placeholder {
    font-size: 1em;
}

.toggle-password-button {
    height: 52px;
    width: 50px;
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

.register-submit-button {
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

.register-submit-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}

.error-Warning {
    text-align: left;
}

.register-submit-button {
    grid-row: register-button;
    background-color: rgba(48, 0, 0);
}

@media only screen and (max-width: 600px) {    
.register-instructions {
    line-height: 150%;
    font-size: 1.2em;
}

.register-form-input {
    font-size: 1.2em;
}

.register-form-input::placeholder {
    font-size: 1em;
}

.register-form-input_username-input {
    width: 300px;
}

.register-form-input_password-input-wrapper {
    grid-template-columns: [password-input] 270px [password-view-toggle-button] 50px;
}

.register-submit-button {
    font-size: 1.2em;
}
}
</style>