<script lang="ts" setup>
interface Props {
    errorString: string
}

const props = defineProps<Props>()
</script>

<template>
  <div class="error-main">
    <div class="error">
      <div class="error-icon-wrapper">
        <img class="error-icon"
          src="@/assets/images/errorIcon.svg"
        />
      </div>

      <p class="error-text">{{ props.errorString }}</p>
    </div>
  </div>
</template>

<style scoped>
.error-main {
  display: flex;
  justify-content: center;
}

.error {
  display: grid;
  grid-template-columns: [error-icon] 10% [error-text] auto;
  border-radius: 5px;
  margin-top: 20px;
  width: 80%;
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
  font-weight: 500;
  margin-left: 10px;
}

@media only screen and (max-width: 600px) {
  .error {
    grid-template-columns: [error-icon] 40px [error-text] 1fr;
    margin-top: 0px;
  }
  .error-text {
    font-size: 1.2em;
  }
}
</style>