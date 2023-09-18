import { ref, Ref } from 'vue'

import { getInfo, getResult } from "@/services/apiService/game/game";

import { Bet, Prediction, RoundInfo, RoundResult } from "@/types/gameElements/gameElementTypes";

export function useRoundInfoComposable() {
    const roundInfo: Ref<RoundInfo> = ref({} as RoundInfo)

    async function updateRoundInfo() {
        try {
            roundInfo.value = await getInfo()
            return roundInfo
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    return { roundInfo, updateRoundInfo }
}

export function useRoundResultComposable() {
    const roundResult: Ref<RoundResult> = ref({} as RoundResult)

    async function updateRoundResult(bet: Bet, prediction: Prediction) {
        try {
            roundResult.value = await getResult(bet, prediction)
            return roundResult
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    return { roundResult, updateRoundResult }
}

export enum GameStates {
    "preGame",
    "welcome",
    "deck",
    "betPrediction",
    "result",
    "gameOver"
}