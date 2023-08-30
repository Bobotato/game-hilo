import { ref, Ref } from 'vue'

import { getInfo, getResult } from "@/services/apiService/game/game";

import { Bet, Prediction, RoundInfo, RoundResult } from "@/types/gameElements/gameElementTypes";
import { Token } from '@/services/apiService/game/game'

export function useRoundInfoComposable() {
    const roundInfo: Ref<RoundInfo> = ref({} as RoundInfo)

    async function getRoundInfo(token: Token) {
        try {
            const roundInfo = await getInfo(token)
            return roundInfo as RoundInfo
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    return { roundInfo, getRoundInfo }
}

export function useRoundResultComposable() {
    const roundResult: Ref<RoundResult> = ref({} as RoundResult)

    async function getRoundResult(token: Token, bet: Bet, prediction: Prediction) {
        try {
            const roundResult = await getResult(token, bet, prediction)
            return roundResult as RoundResult
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    return { roundResult, getRoundResult }
}