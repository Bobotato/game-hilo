<script lang="ts" setup>
interface Props {
    itemName: string
    itemQuantity: number
    itemImageSource: string
}

const props = withDefaults(defineProps<Props>(), {
    itemName: "Test Item",
    itemQuantity: 0,
    itemImageSource: `../../assets/images/TestItem.png`
})

function getImageUrl() {
    return new URL(`${props.itemImageSource}`, import.meta.url).href
}
</script>

<template>
    <div class="receive-item-wrapper">
        <div class="receive-item-card">
            <div class="item-wrapper">
                <img class="item-image" :src="getImageUrl()" :alt="props.itemName">
                <h2 class=" item-desc">{{ props.itemName }}</h2>
            </div>
        </div>
    </div>
</template>

<style>
.receive-item-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

.receive-item-card {
    width: 100px;
    background-color: rgba(255, 255, 255, 0.35);
}

.item-image {
    width: 300px;
    height: 300px;
}

.item-desc {
    text-align: center;
    font-size: 1.5em;
    color: white;
}
</style>