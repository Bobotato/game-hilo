import { ref, Ref } from 'vue'

import { postLogin, postRegister } from "@/services/apiService/user/user";
import { Credentials } from '@/services/apiService/user/user'

export function useAuthComposable() {
    const getCredentialsForm: Ref<Credentials> = ref({} as Credentials)

    async function loginAccount(credentials: Credentials) {
        return await postLogin(credentials)
    }

    async function registerAccount(credentials: Credentials) {
        return await postRegister(credentials)
    }

    return { getCredentialsForm, loginAccount, registerAccount }
}