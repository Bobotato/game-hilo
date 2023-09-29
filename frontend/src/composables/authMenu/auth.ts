import { ref, Ref } from 'vue'

import { postLogin, postRegister } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function useAuthComposable() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function loginAccount(credentials: Credentials) {
        try {
            return await postLogin(credentials)
        } catch (error: any) {
            console.error('Login failed with error:', `${error}`)
            throw error
        }
    }


    async function registerAccount(credentials: Credentials) {
        try {
            return await postRegister(credentials)
        } catch (error: any) {
            console.error('Registration failed with error:', `${error}`)
            throw error
        }
    }

    return { getCredentialsForm, loginAccount, registerAccount }
}