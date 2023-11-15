<script lang="ts" setup>
</script>

<template>
    <main class="loading-main">
        <p class="loading-message">Loading...</p>
    </main>
</template>

<style>
.loading-main {
    z-index: 999;
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0);
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

@media only screen and (max-width: 600px) {
.loading-message {
    font-size: 1.2em;
}
} 
</style>