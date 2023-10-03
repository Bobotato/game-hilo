import { router } from '@/router/index'
import { postLogout } from '@/services/apiService/user/user'

export function logOut() {
    postLogout()
    router.push({ path: '/login' })
}