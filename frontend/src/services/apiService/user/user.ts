import { apiClient } from '@/services/apiService/axiosClient'
import {
  APIServerDownError,
  AuthenticationError,
  APIResponseMalformedError,
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

export async function attemptLogin(credentials: Credentials): Promise<LoginResponse> {
  try {
    const requestBody = {
      username: credentials.username,
      password: credentials.password
    };

    const response = await apiClient.post('/user/authenticate',
      requestBody,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      },
    )
    LoginResponseSchema.parse(response.data)
    return response.data as LoginResponse
  } catch (error: any) {
    if (error instanceof AxiosError && error.response) {
      switch (error.response.status) {
        case 403:
          throw new AuthenticationError('Credentials are invalid')
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

export async function attemptRegister(credentials: Credentials): Promise<RegisterResponse> {
  try {
    const requestBody = {
      username: credentials.username,
      password: credentials.password
    };

    const response = await apiClient.post('/user/register',
      requestBody,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      },
    )
    RegisterResponseSchema.parse(response.data)
    return response.data as RegisterResponse

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
