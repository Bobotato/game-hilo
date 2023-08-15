<script lang="ts" setup>
interface Props {
    itemName: string
    itemQuantity?: number
    itemImageSource: string
}

const props = withDefaults(defineProps<Props>(), {
    itemName: "Test Item",
    itemImageSource: `../../assets/images/TestItem.png`
})

function getImageUrl() {
    return new URL(`${props.itemImageSource}`, import.meta.url).href
}
</script>

<template>
    <div class="receive-item-wrapper">
        <div class="receive-item-card">
            <h2 class="item-receive-text">You have received:</h2>
            <div class="item-wrapper">
                <img class="item-image" :src="getImageUrl()" :alt="props.itemName">
                <h2 class="item-receive-text">{{ props.itemQuantity }}</h2>
                <h2 class="item-receive-text">{{ props.itemName }}</h2>
            </div>
        </div>
    </div>
</template>

<style>
.receive-item-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
}

.receive-item-card {
    display: grid;
    grid-template-rows: [item-receive-text] auto [item-image] auto [item-receive-qty] auto [item-name] auto;
    align-items: center;
    justify-content: center;
    width: 1000px;
}

.item-receive-text {
    text-align: center;
    font-size: 1.5em;
    color: white;
}

.item-image {
    height: 300px;
}

.item-desc {
    text-align: center;
    font-size: 1.5em;
    color: white;
}
</style>