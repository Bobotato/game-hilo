import menuSelect from '@/assets/sounds/foleyAudio/menuSelect.mp3'
import errorBuzzer from '@/assets/sounds/foleyAudio/errorBuzzer.mp3'
import menuTheme from '@/assets/sounds/bgmAudio/menuTheme.mp3'
import gameTheme from '@/assets/sounds/bgmAudio/gameTheme.mp3'
import enterConfirm from '@/assets/sounds/foleyAudio/enterConfirm.mp3'
import choiceSelect from '@/assets/sounds/foleyAudio/choiceSelect.mp3'
import menuReturn from '@/assets/sounds/foleyAudio/menuReturn.mp3'

export class AudioPlayer {
  bgmAudio: any
  foleyAudio: any
  volume: number
  isMuted: boolean

  constructor(bgmAudio: any = null, foleyAudio: any = null, volume: number = 0.1, isMuted: boolean = false) {
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
      case (sound = "gameThemeSfx"):
        this.playBGMAudio(gameTheme)
        break
      case (sound = "errorBuzzer"):
        this.playFoleyAudio(errorBuzzer)
        break
      case (sound = "enterConfirmSfx"):
        this.playFoleyAudio(enterConfirm)
        break
      case (sound = "choiceSelectSfx"):
        this.playFoleyAudio(choiceSelect)
        break
      case (sound = "menuReturnSfx"):
        this.playFoleyAudio(menuReturn)
        break
    }
  }

  playBGMAudio(sound: any) {
    if (sound) {
      this.bgmAudio = new Audio(sound);
      this.bgmAudio.volume = this.volume;
      this.bgmAudio.muted = this.isMuted;
      this.bgmAudio.loop = true
      this.bgmAudio.play();
    }
  }

  playFoleyAudio(sound: string) {
    if (sound) {
      this.foleyAudio = new Audio(sound);
      this.foleyAudio.volume = this.volume;
      this.foleyAudio.muted = this.isMuted;
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
    if (this.bgmAudio !== null) {
      this.bgmAudio.pause()
    }
  }

  updateMute() {
    if (this.bgmAudio !== null) {
      this.bgmAudio.muted = this.isMuted;
    }
    if (this.foleyAudio !== null) {
      this.foleyAudio.muted = this.isMuted;
    }
  }
}