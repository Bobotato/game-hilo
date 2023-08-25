import { attemptLogin } from "@/services/apiService/user/user";
import { attemptRegister } from "@/services/apiService/user/user";

export async function tryLogin(credentials) {
    const response = await attemptLogin(credentials)
    return response
}