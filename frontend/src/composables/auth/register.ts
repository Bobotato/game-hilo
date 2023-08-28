import { ref, Ref } from 'vue'

import { postRegister } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function register() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function tryRegister(credentials: Credentials) {
        try {
            const response = await postRegister(credentials)
            return response

        } catch (error: any) {
            console.log('Registration failed with error:', `${error}`)
            throw error
        }
    }

    return { getCredentialsForm, tryRegister }
}