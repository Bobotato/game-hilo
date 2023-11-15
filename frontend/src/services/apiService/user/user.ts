import { AxiosError } from 'axios'
import { ZodError } from 'zod'

import { apiClient } from '@/services/apiService/axiosClient'
import {
  APIServerDownError,
  InvalidCredentialsError,
  APIResponseMalformedError,
  UsernameAlreadyExistsError
} from '@/services/apiService/errors'
import { gameErrorCodes } from '@/services/apiService/game/game'
import { LoginResponseSchema, RegisterResponseSchema } from '@/schemas/schemas'

const authErrorCodes: { [key: number]: Error } = { 
  401: new InvalidCredentialsError('Credentials are invalid'),
  409: new UsernameAlreadyExistsError('User already exists'),
  500: new APIServerDownError('API Server down'), }

export interface Credentials {
  username: string
  password: string
}

export interface RegisterResponse {
  access_token: string
}

export interface LoginResponse {
  access_token: string
}

export async function postLogin(credentials: Credentials): Promise<LoginResponse> {
  try {
    const {data} = await apiClient.post('/user/authenticate', credentials)
    LoginResponseSchema.parse(data)
    return data as LoginResponse

  } catch (error: any) {
    if (error instanceof AxiosError && error.response && error.response.status in authErrorCodes) {
      throw (authErrorCodes[error.response.status])
    } else if (error instanceof ZodError) {
      throw new APIResponseMalformedError('API returned malformed response')
    } else {
      throw error
    }
  }
}

export async function postRegister(credentials: Credentials): Promise<RegisterResponse> {
  try {
    const {data} = await apiClient.post('/user/register', credentials)
    RegisterResponseSchema.parse(data)
    return data as RegisterResponse

  } catch (error: any) {
    if (error instanceof AxiosError && error.response && error.response.status in authErrorCodes) {
      throw (authErrorCodes[error.response.status])
    } else if (error instanceof ZodError) {
      throw new APIResponseMalformedError('API returned malformed response')
    } else {
      throw error
    }
  }
}

export async function postLogout(): Promise<void> {
    try {
      await apiClient.post('/user/logout')
    } catch (error: any) {
      if (error instanceof AxiosError && error.response && error.response.status in gameErrorCodes) {
        throw (gameErrorCodes[error.response.status])
        } else {
            throw error
        }
    }
}

export async function verifyJWT(): Promise<void> {
  try {
    await apiClient.post('/user/verify-token')
  } catch (error: any) {
      if (error instanceof AxiosError && error.response && error.response.status in gameErrorCodes) {
        throw (gameErrorCodes[error.response.status])
    } else {
        throw error
    }
  }
}