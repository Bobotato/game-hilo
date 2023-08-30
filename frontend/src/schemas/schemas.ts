import { z } from 'zod'

export const RegisterResponseSchema = z.object({
    access_token: z.string()
})

export const LoginResponseSchema = z.object({
    access_token: z.string()
})

const Player = z.object({
    name: z.string(),
    credits: z.number(),
})

const Card = z.object({
    sort_index: z.number(),
    rank: z.number(),
    suit: z.number()
})

export const InfoResponseSchema = z.object({
    player: Player,
    current_card: Card
})

export const ResultResponseSchema = z.object({
    drawn_card: Card,
    win: z.boolean(),
    is_player_bankrupt: z.boolean(),
    is_deck_empty: z.boolean()
})