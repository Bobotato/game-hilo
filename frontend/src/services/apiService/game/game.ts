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
import { Prediction } from '@/models/betPrediction'
import { Card, Player } from "@/types/gameElements/gameElementTypes"

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
        if (error instanceof AxiosError && error.response) {
            switch (error.response.status) {
                case 401:
                    throw new UnauthorisedError('Token is invalid')
                case 500:
                    throw new APIServerDownError('API Server down')
                default:
                    throw new Error(`Something went wrong with the API response, the error is: ${error}}`)
            }
        } else if (error instanceof ZodError) {
            throw new APIResponseMalformedError('API returned malformed response')
        } else {
            throw error
        }
    }
}

export async function getResult(bet: number, prediction: Prediction): Promise<ResultResponse> {
    try {
        const response = await apiClient.post('/game/result', {}, {
            params: {
                bet: bet,
                prediction: prediction
            }
        })
        ResultResponseSchema.parse(response.data)
        return response.data as ResultResponse
    } catch (error: any) {
        if (error instanceof AxiosError && error.response) {
            switch (error.response.status) {
                case 401:
                    throw new UnauthorisedError('Token is invalid')
                case 404:
                    throw new NoSuchGameError('There is no ongoing game associated with this account')
                case 500:
                    throw new APIServerDownError('API Server down')
                default:
                    throw new Error(`Something went wrong with the API response, the error is: ${error}}`)
            }
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
        if (error instanceof AxiosError && error.response) {
            switch (error.response.status) {
                case 401:
                    throw new UnauthorisedError('Token is invalid')
                case 500:
                    throw new APIServerDownError('API Server down')
                default:
                    throw new Error(`Something went wrong with the API response, the error is: ${error}}`)
            }
        } else {
            throw error
        }
    }
}