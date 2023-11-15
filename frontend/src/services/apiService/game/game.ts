import { AxiosError } from 'axios'
import { ZodError } from 'zod'

import { apiClient } from '@/services/apiService/axiosClient'
import {
    APIServerDownError,
    UnauthorisedError,
    APIResponseMalformedError,
    NoSuchGameError
} from '@/services/apiService/errors'
import { InfoResponseSchema, ResultResponseSchema } from '@/schemas/schemas'
import { BetPrediction } from '@/components/game/BetPage.vue';
import { Card, Player } from "@/types/gameElements/gameElementTypes"

export const gameErrorCodes: { [key: number]: Error } = { 
    401: new UnauthorisedError('Token is invalid'),
    404: new NoSuchGameError('There is no ongoing game associated with this account'),
    500: new APIServerDownError('API Server down'), }

export interface Token {
    access_token: string
}

export interface InfoResponse {
    player: Player,
    current_card: Card
}

export interface ResultResponse {
    drawn_card: Card,
    win: boolean,
    is_player_bankrupt: boolean,
    is_deck_empty: boolean
}

export async function getInfo(): Promise<InfoResponse> {
    try {
        const response = await apiClient.post('/game/info')
        InfoResponseSchema.parse(response.data)
        return response.data as InfoResponse
    } catch (error: any) {
        if (error instanceof AxiosError && error.response && error.response.status in gameErrorCodes) {
            throw (gameErrorCodes[error.response.status])
        } else if (error instanceof ZodError) {
            throw new APIResponseMalformedError('API returned malformed response')
        } else {
            throw error
        }
    }
}

export async function getResult(betPrediction: BetPrediction): Promise<ResultResponse> {
    try {
        const response = await apiClient.post('/game/result', {}, {
            params: {
                bet: betPrediction.bet,
                prediction: betPrediction.prediction
            }
        })
        ResultResponseSchema.parse(response.data)
        return response.data as ResultResponse
    } catch (error: any) {
        if (error instanceof AxiosError && error.response && error.response.status in gameErrorCodes) {
            throw (gameErrorCodes[error.response.status])
        } else if (error instanceof ZodError) {
            throw new APIResponseMalformedError('API returned malformed response')
        } else {
            throw error
        }
    }
}

export async function resetGame(): Promise<void> {
    try {
        await apiClient.post('/game/reset')
    } catch (error: any) {
        if (error instanceof AxiosError && error.response && error.response.status in gameErrorCodes) {
            throw (gameErrorCodes[error.response.status])
        } else {
            throw error
        }
    }
}