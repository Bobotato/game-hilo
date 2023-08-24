import { apiClient } from '@/services/apiService/axiosClient'

interface Token {
    token: string
}

export async function getInfo(token: Token) {
    try {
        const response = await apiClient.post('/game/info')
        return response
    } catch (error: any) {
        console.log(error)
    }
}

export async function getResult(token: Token, bet: Bet, prediction: Prediction) {
    try {
        const response = await apiClient.post('/game/result', {
            params: {
                bet: bet,
                prediction: prediction
            }
        })
        return response
    } catch (error: any) {
        console.log(error)
    }
}