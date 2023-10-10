import { ref, Ref } from 'vue'

import { getInfo, getResult } from "@/services/apiService/game/game";

import { RoundInfo, RoundResult } from "@/types/gameElements/gameElementTypes";
import { BetPrediction } from '@/components/game/BetPage';

export function useGame() {
    const roundInfo: Ref<RoundInfo> = ref({} as RoundInfo)
    const roundResult: Ref<RoundResult> = ref({} as RoundResult)

    async function updateRoundInfo() {
        try {
            roundInfo.value = await getInfo()
            return roundInfo
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    async function updateRoundResult(betPrediction: BetPrediction) {
        try {
            roundResult.value = await getResult(betPrediction)
            return roundResult
        } catch (error: any) {
            console.log(`RoundInfo retrieval failed with error ${error}`)
            throw error
        }
    }

    return { roundInfo, roundResult, updateRoundInfo, updateRoundResult }
}