import { apiClient } from '@/services/apiService/axiosClient'
import {
  APIServerDownError,
  AuthenticationError,
  APIResponseMalformedError,
  UsernameAlreadyExistsError
} from '@/services/apiAuthService/errors'
import { AxiosError } from 'axios'
import { ZodError } from 'zod'

interface Credentials {
  username: string
  password: string
}

export async function attemptLogin(credentials: Credentials) {
  try {
    const response = await apiClient.post('/user/authenticate')
    return response
  } catch (error: any) {
    console.log(error)
  }
}

export async function attemptRegister(credentials: Credentials) {
  try {
    const response = await apiClient.post('/user/register')
    return response
  } catch (error: any) {
    console.log(error)
  }
}



// export interface CurrentWeatherForm {
//   searchCity: string
// }

// export interface ForecastWeatherForm {
//   searchCity: string
//   length: number
// }

// export async function getCurrentWeather(form: CurrentWeatherForm): Promise<CurrentWeatherResponse> {
//   try {
//     const response = await apiClient.get('/current.json', {
//       params: {
//         q: form.searchCity,
//         aqi: 'no'
//       }
//     })
//     CurrentWeatherResponseSchema.parse(response.data)
//     return response.data as CurrentWeatherResponse
//   } catch (error: any) {
//     if (error instanceof AxiosError && error.response) {
//       switch (error.response.status) {
//         case 400:
//           throw new NoMatchingCityError('Search returned no results')
//         case 403:
//           throw new APIAuthenticationError('API Key invalid')
//         case 500:
//           throw new APIServerDownError('API Server down')
//         default:
//           throw new Error(`Something went wrong with the API response, the error is: ${error}}`)
//       }
//     } else if (error instanceof ZodError) {
//       throw new APIResponseMalformedError('API returned malformed response')
//     } else {
//       throw error
//     }
//   }
// }

// export async function loginRequest(form: ForecastWeatherForm): Promise<ForecastWeatherResponse> {
//   try {
//     const response = await apiClient.get('/forecast.json', {
//       params: {
//         q: form.searchCity,
//         days: 3,
//         aqi: 'no',
//         alerts: 'no'
//       }
//     })
//     ForecastWeatherResponseSchema.parse(response.data)
//     return response.data as ForecastWeatherResponse
//   } catch (error: any) {
//     if (error instanceof AxiosError && error.response) {
//       switch (error.response.status) {
//         case 400:
//           throw new NoMatchingCityError('Search returned no results')
//         case 403:
//           throw new APIAuthenticationError('API Key invalid')
//         case 500:
//           throw new APIServerDownError('API Server down')
//         default:
//           throw new Error(`Something went wrong with the API response, the error is: ${error}}`)
//       }
//     } else if (error instanceof ZodError) {
//       console.log(error)
//       throw new APIResponseMalformedError('API returned malformed response')

//     } else {
//       throw error
//     }
//   }
// }
