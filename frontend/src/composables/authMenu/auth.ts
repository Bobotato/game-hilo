import { ref, Ref } from 'vue'

import { postLogin, postRegister } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function useAuthComposable() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function tryLogin(credentials: Credentials) {
        try {
            return await postLogin(credentials)
        } catch (error: any) {
            console.error('Login failed with error:', `${error}`)
            throw error
        }
    }


    async function tryRegister(credentials: Credentials) {
        try {
            return await postRegister(credentials)
        } catch (error: any) {
            console.error('Registration failed with error:', `${error}`)
            throw error
        }
    }

    return { getCredentialsForm, tryLogin, tryRegister }
}