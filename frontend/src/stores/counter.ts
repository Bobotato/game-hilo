import { ref } from 'vue'
import { defineStore } from 'pinia'

export const isMuted = defineStore('isMuted', () => {
  const isMuted = ref(false)
  function toggleIsMuted() {
    isMuted.value = !isMuted.value
  }

  return { isMuted, toggleIsMuted }
})
