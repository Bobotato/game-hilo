import menuSelect from '@/assets/sounds/foleyAudio/menuSelect.mp3'
import menuTheme from '@/assets/sounds/bgmAudio/menuTheme.mp3'

export class AudioPlayer {
  bgmAudio: any
  foleyAudio: any
  volume: number
  isMuted: boolean

  constructor(bgmAudio: any = "", foleyAudio: any = "", volume: number = 0.1, isMuted: boolean = false) {
    this.bgmAudio = bgmAudio
    this.foleyAudio = foleyAudio
    this.volume = volume
    this.isMuted = isMuted
  }

  playAudio(sound: string) {
    switch (sound) {
      case (sound = "menuSelectSfx"):
        this.playFoleyAudio(menuSelect)
        break
      case (sound = "menuThemeSfx"):
        this.playBGMAudio(menuTheme)
        break
    }
  }

  playBGMAudio(sound: any) {
    if (sound) {
      this.bgmAudio = new Audio(sound);
      this.bgmAudio.volume = this.volume;
      this.bgmAudio.play();
    }
  }

  playFoleyAudio(sound: string) {
    if (sound) {
      this.foleyAudio = new Audio(sound);
      this.foleyAudio.volume = this.volume;
      this.foleyAudio.play();
    }
  }

  printWorking() {
    console.log('wwokring')
  }

  toggleMuteAudio() {
    this.isMuted = !this.isMuted
    this.updateMute()
  }

  stopAudio() {
    if (this.bgmAudio !== "") {
      this.bgmAudio.pause()
    }
    if (this.foleyAudio !== "") {
      this.foleyAudio.pause()
    }
  }

  updateMute() {
    this.bgmAudio.muted = this.isMuted;
    this.foleyAudio.muted = this.isMuted;
  }
}