<script lang="ts" setup>
import { ref, Ref } from 'vue'

const emit = defineEmits<{
    (e: 'playAudio', sound: string): void
    (e: 'getBet', bet: number): void
    (e: 'getPrediction', prediction: string): void
}>()

let bet = ref()
let prediction: <Ref>string = ref("")

function submitInputs() {
}
</script>

<template></template>

<style></style>