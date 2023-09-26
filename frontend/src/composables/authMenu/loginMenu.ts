import { ref, Ref } from 'vue'

import { postLogin } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function useLoginComposable() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function tryLogin(credentials: Credentials) {
        try {
            return await postLogin(credentials)
        } catch (error: any) {
            console.error('Login failed with error:', `${error}`)
            throw error
        }
    }

    return { getCredentialsForm, tryLogin }
}