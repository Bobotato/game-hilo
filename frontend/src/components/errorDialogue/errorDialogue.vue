<script lang="ts" setup>
defineProps<{
  errorMessage: string
}>()
</script>

<template>
  <div class="error_wrapper">
    <div class="error">
      <div class="error_icon_wrapper">
        <img class="error_icon" src="@/assets/images/errorIcon.svg" />
      </div>
      <p class="error_text">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<style>
.error_wrapper {
  display: flex;
  justify-content: center;
}

.error {
  display: grid;
  grid-template-columns: [error_icon] 10% [error_text] auto;
  border-radius: 5px;
  margin-top: 20px;
  width: 80%;
}

.error_icon_wrapper {
  display: flex;
  grid-column: error_icon;
  justify-content: center;
  align-items: center;
}

.error_icon {
  width: 30px;
  height: 30px;
}

.error_text {
  color: red;
  font-weight: 500;
  margin-left: 10px;
}

@media screen and (min-width: 1000px) {
  .error_wrapper {
    display: flex;
    justify-content: center;
  }

  .error {
    display: grid;
    grid-template-columns: [error_icon] 40px [error_text] 1fr;
    border-radius: 5px;
    margin-top: 0px;
    width: 100%;
  }

  .error_icon_wrapper {
    display: flex;
    grid-column: error_icon;
    justify-content: center;
    align-items: center;
  }

  .error_icon {
    width: 30px;
    height: 30px;
  }

  .error_text {
    display: flex;
    max-width: 600px;
    justify-content: flex-start;
    align-items: center;
    grid-column: error_text;
    margin-left: 10px;
    color: red;
    font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu,
    Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
    font-size: 1.3em;
  }
}
</style>