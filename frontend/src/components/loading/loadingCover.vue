<script lang="ts" setup>
</script>

<template>
    <div class="loading-cover">
        <p class="loading-message">Loading...</p>
    </div>
</template>

<style>
.loading-cover {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100vw;
    height: 100vh;
    background: black;
}

.loading-message {
    font-size: 1.5em;
    color: white;
    clip-path: inset(0 1.6ch 0 0);
    animation: l 1s steps(4) infinite;
}

@keyframes l {
    to {
        clip-path: inset(0 -0.63ch 0 0)
    }
}
</style>