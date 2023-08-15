import menuSelect from '@/assets/sounds/menuSelect.mp3'
import menuTheme from '@/assets/sounds/menuTheme.mp3'

export class AudioPlayer {
  audio: any
  volume: number
  isMuted: boolean

  constructor(audio: any = "", volume: number = 0.1, isMuted: boolean = false) {
    this.audio = audio
    this.volume = volume
    this.isMuted = isMuted
  }

  playAudio(sound: any) {
    if (sound) {
      this.audio = new Audio(sound);
      this.audio.volume = this.volume;
      this.audio.play();
    }
  }

  menuSelectSfx() {
    this.playAudio(menuSelect)
  }

  menuThemeSfx() {
    this.playAudio(menuTheme)
  }

  toggleMuteAudio() {
    if (this.isMuted == false) {
      this.isMuted = true
      this.volume = 0
    }
    else {
      this.isMuted = false
      this.volume = 0.1
    }
  }

  stopAudio() {
    this.audio.stop()
  }
}