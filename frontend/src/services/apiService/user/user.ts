import { apiClient } from '@/services/apiService/axiosClient'
import {
  APIServerDownError,
  InvalidCredentialsError,
  APIResponseMalformedError,
  UnauthorisedError,
  UsernameAlreadyExistsError
} from '@/services/apiService/errors'
import { AxiosError } from 'axios'
import { ZodError } from 'zod'
import { LoginResponseSchema, RegisterResponseSchema } from '@/schemas/schemas'
import { LoginResponse, RegisterResponse } from '@/types/apiResponseTypes'

export interface Credentials {
  username: string
  password: string
}

export async function postLogin(credentials: Credentials): Promise<LoginResponse> {
  try {
    const {data} = await apiClient.post('/user/authenticate', credentials)
    LoginResponseSchema.parse(data)
    return data as LoginResponse
  } catch (error: any) {
    if (error instanceof AxiosError && error.response) {
      switch (error.response.status) {
        case 401:
          throw new InvalidCredentialsError('Credentials are invalid')
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

export async function postRegister(credentials: Credentials): Promise<RegisterResponse> {
  try {
    const {data} = await apiClient.post('/user/register', credentials)
    RegisterResponseSchema.parse(data)
    return data as RegisterResponse

  } catch (error: any) {
    if (error instanceof AxiosError && error.response) {
      switch (error.response.status) {
        case 409:
          throw new UsernameAlreadyExistsError('User already exists')
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

export async function postLogout(): Promise<void> {
    try {
      await apiClient.post('/user/logout')
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

export async function verifyJWT(): Promise<void> {
  try {
    await apiClient.post('/user/verify-token')
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