import menuSelect from '@/assets/sounds/menuSelect.mp3'

function playSound (sound: any) {
    if(sound) {
      const audio = new Audio(sound);
      audio.play();
    }
}

export function menuSelectSfx () {
    playSound(menuSelect)
}
