import { Card, Player } from "./gameElements/gameElementTypes"

export interface RegisterResponse {
    access_token: string
}

export interface LoginResponse {
    access_token: string
}

export interface InfoResponse {
    player: Player,
    current_card: Card
}

export interface ResultResponse {
    drawn_card: Card,
    win: boolean,
    is_player_bankrupt: boolean,
    is_deck_empty: boolean
}