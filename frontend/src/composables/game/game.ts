import { ref, Ref } from 'vue'

import { getInfo, getResult } from "@/services/apiService/game/game";

import { RoundInfo, RoundResult } from "@/types/gameElements/gameElementTypes";
import { BetPrediction } from '@/components/game/BetPage.vue';

export function useGame() {
    const roundInfo: Ref<RoundInfo> = ref({} as RoundInfo)
    const roundResult: Ref<RoundResult> = ref({} as RoundResult)

    async function updateRoundInfo() {
        roundInfo.value = await getInfo()
        return roundInfo

    }

    async function updateRoundResult(betPrediction: BetPrediction) {
        roundResult.value = await getResult(betPrediction)
        return roundResult
    }

    return { roundInfo, roundResult, updateRoundInfo, updateRoundResult }
}