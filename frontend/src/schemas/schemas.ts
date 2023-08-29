import { z } from 'zod'

export const RegisterResponseSchema = z.object({
    access_token: z.string()
})

export const LoginResponseSchema = z.object({
    access_token: z.string()
})

export const InfoResponseSchema = z.object({
    player: z.string(),
    current_card: z.string()
})

export const ResultResponseSchema = z.object({
    drawn_card: z.string(),
    win: z.boolean(),
    is_player_bankrupt: z.boolean(),
    is_deck_empty: z.boolean()
})