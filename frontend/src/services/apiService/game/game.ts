import { apiClient } from '@/services/apiService/axiosClient'
import {
    APIServerDownError,
    UnauthorisedError,
    APIResponseMalformedError,
    NoSuchGameError
} from '@/services/apiService/errors'
import { AxiosError } from 'axios'
import { ZodError } from 'zod'
import { InfoResponseSchema, ResultResponseSchema } from '@/schemas/schemas'
import { InfoResponse, ResultResponse } from '@/types/apiResponseTypes'
import { Bet, Prediction } from '@/types/gameElements/gameElementTypes'

export interface Token {
    access_token: string
}

export async function getInfo(token: Token): Promise<InfoResponse> {
    try {
        console.log(token)
        const requestBody = {
            access_token: token.access_token
        };

        const response = await apiClient.post('/game/info',
            requestBody,
            {
                headers: {
                    'Content-Type': 'application/json',
                },
            },
        )
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

export async function getResult(token: Token, bet: Bet, prediction: Prediction): Promise<ResultResponse> {
    try {
        const requestBody = {
            access_token: token.access_token
        };

        const response = await apiClient.post('/game/result',
            requestBody,
            {
                params: {
                    bet: bet,
                    prediction: prediction
                },
                headers: {
                    'Content-Type': 'application/json',
                },
            },
        )
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