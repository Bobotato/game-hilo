import { attemptLogin } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export async function tryLogin(credentials: Credentials) {
    try {
        const response = await attemptLogin(credentials)
        return response
    } catch (error: any) {
        console.log('Login failed with error:', `${error}`)
        throw error
    }
}