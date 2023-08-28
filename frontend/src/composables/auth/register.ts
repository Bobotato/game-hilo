import { attemptRegister } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export async function tryRegister(credentials: Credentials) {
    try {
        const response = await attemptRegister(credentials)
        return response
    } catch (error: any) {
        console.log('Registration failed with error:', `${error}`)
        throw error
    }
}