<script lang="ts" setup>
let description = "This game might be slightly spooky, with spooky sounds and dismembered bits. \n Use the mute icon on the bottom right to disable sounds."
</script>

<template>
    <div class="bg">
        <div class="description-card">
            <h2 class="description">{{ description }}</h2>
            <RouterLink to="/login">
                <button class="continue-button" @click="$emit('play-audio', 'menu-select')">Continue</button>
            </RouterLink>
        </div>
    </div>
</template>

<style scoped>
.bg {
    justify-content: center;
    align-items: center;
    background-color: black;
}

.description-card {
    display: grid;
    justify-items: center;
    align-items: center;
    text-align: center;
    grid-template-rows: [description-text] auto [continue-button] auto;
}

.description {
    line-height: 200%;
    font-size: 1.5em;
    white-space: pre-wrap;
    text-align: center;
    color: white;
}

.continue-button {
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

.continue-button:hover {
    box-shadow: 0px 0px 5px rgba(255, 255, 255, 0.8);
}
</style>