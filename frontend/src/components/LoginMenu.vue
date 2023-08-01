<script lang="ts" setup>
import { ref } from 'vue'
import { menuSelectSfx } from '@/services/SoundPlayerService'
import errorDialogue from '@/components/errorDialogue/errorDialogue.vue'


let passwordInput = ref({
    showPassword: false,
    password: null
})

let errorHeader = ref({
  message: '',
})

function togglePasswordShow() {
    passwordInput.value.showPassword = !passwordInput.value.showPassword
}
</script>

<template>
    <div class="login-component">
        <div class="login-menu">
            <div class="welcome-message">
                Welcome to Alex's hi-lo game.
                Please log-in or register.
            </div>

            <input autofocus
            type="text"
            class="input username-input"
            placeholder="Username"
            required>

            <div class="password-input-wrapper">
                <input v-if="passwordInput.showPassword" type="text" class="input password-input" v-model="passwordInput.password" placeholder="Password"/>
                <input v-else type="password" class="input password-input" v-model="passwordInput.password" placeholder="Password">

                <button :class="{'toggle-password-button password-shown': passwordInput.showPassword, 'toggle-password-button password-hidden': !passwordInput.showPassword}" @click="togglePasswordShow"></button>
            </div>

            <errorDialogue
            class="error_dialogue"
            v-if="errorHeader.message !== ''"
            :errorMessage="errorHeader.message"
            ></errorDialogue>

            <button class="button login-button" @click="menuSelectSfx">
                Log In
            </button>

            <button class="button register-button" @click="menuSelectSfx">
                Register
            </button>
        </div>
    </div>
</template>

<style scoped>
.login-component {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.login-menu {
    display: grid;
    width: 40%;
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
    width: 30%;
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
</style>