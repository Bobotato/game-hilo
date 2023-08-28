import { ref, Ref } from 'vue'

import { postLogin } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function login() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function tryLogin(credentials: Credentials) {
        try {
            const response = await postLogin(credentials)
            return response

        } catch (error: any) {
            console.log('Login failed with error:', `${error}`)
            throw error
        }
    }

    return { getCredentialsForm, tryLogin }
}