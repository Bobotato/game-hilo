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

@media screen and (min-width: 1000px) {
  .error-main {
    display: flex;
    justify-content: center;
  }

  .error {
    display: grid;
    grid-template-columns: [error-icon] 40px [error-text] 1fr;
    border-radius: 5px;
    margin-top: 0px;
    width: 100%;
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
    display: flex;
    max-width: 600px;
    justify-content: flex-start;
    align-items: center;
    grid-column: error-text;
    margin-left: 10px;
    color: red;
    font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu,
    Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
    font-size: 1.3em;
  }
}
</style>