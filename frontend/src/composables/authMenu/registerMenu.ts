import { ref, Ref } from 'vue'

import { postRegister } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function useRegisterComposable() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function tryRegister(credentials: Credentials) {
        try {
            return await postRegister(credentials)
        } catch (error: any) {
            console.error('Registration failed with error:', `${error}`)
            throw error
        }
    }

    return { getCredentialsForm, tryRegister }
}