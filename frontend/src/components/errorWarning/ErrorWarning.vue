<script lang="ts" setup>
interface Props {
    errorString: string
}

const props = defineProps<Props>()
</script>

<template>
  <main class="error-main">
    <div class="error">
      <div class="error-icon-wrapper">
        <img class="error-icon"
          src="@/assets/images/errorIcon.svg"/>
      </div>

      <p class="error-text">{{ props.errorString }}</p>
    </div>
  </main>
</template>

<style scoped>
.error-main {
  display: flex;
  justify-content: center;
}

.error {
  display: grid;
  align-items: center;
  grid-template-columns: [error-icon] auto [error-text] auto;
  border-radius: 5px;
  margin: 20px 0 0 0;
}

.error-icon-wrapper {
  display: flex;
  grid-column: error-icon;
  justify-content: center;
  align-items: center;
}

.error-icon {
  width: 30px;
  height: 30px;
}

.error-text {
  color: red;
  font-size: 1.5em;
  font-weight: 500;
  margin: 0 0 0 20px;
}

@media only screen and (max-width: 600px) {
  .error {
    grid-template-columns: [error-icon] 40px [error-text] 1fr;
    margin-top: 0px;
  }
  .error-text {
    font-size: 1.2em;
    margin: 0 0 0 10px;
  }
}
</style>