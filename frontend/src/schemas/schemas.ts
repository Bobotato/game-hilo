import { z } from 'zod'

export const RegisterResponseSchema = z.object({
    access_token: z.string()
})

export const LoginResponseSchema = z.object({
    access_token: z.string()
})