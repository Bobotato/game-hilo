<script lang="ts" setup>
let description = "This game might be slightly spooky, with spooky sounds and dismembered bits. \n Use the mute icon on the bottom right to disable sounds."
</script>

<template>
    <div class="bg">
        <div class="description-card">
            <h2 class="description">{{ description }}</h2>
            <RouterLink to="/login">
                <button class="continue-button">Continue</button>
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
    width: 300px;
    color: white;
    background-color: rgba(48, 0, 0, 80%);
}
</style>