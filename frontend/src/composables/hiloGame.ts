import { ref, Ref } from 'vue'

import { getInfo, getResult } from "@/services/apiService/game/game";

import { Bet, Prediction, RoundInfo, RoundResult } from "@/types/gameElements/gameElementTypes";
import { Token } from '@/services/apiService/game/game'

export function useRoundInfoComposable() {
    const roundInfo: Ref<RoundInfo> = ref({} as RoundInfo)

    async function updateRoundInfo(token: Token) {
        try {
            roundInfo.value = await getInfo(token)
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

    async function updateRoundResult(token: Token, bet: Bet, prediction: Prediction) {
        try {
            roundResult.value = await getResult(token, bet, prediction)
            return roundResult
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    return { roundResult, updateRoundResult }
}