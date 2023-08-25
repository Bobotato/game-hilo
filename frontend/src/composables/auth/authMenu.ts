import { attemptLogin } from "@/services/apiService/user/user";
import { attemptRegister } from "@/services/apiService/user/user";

export async function tryLogin(credentials) {
    const credentials2 = { username: "string", password: "string" }
    const response = await attemptLogin(credentials2)
    console.log(response)
}

export async function tryRegister(credentials) {
    const credentials2 = { username: "string", password: "string" }
    const response = await attemptRegister(credentials2)
    return response
}