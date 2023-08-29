export interface RegisterResponse {
    access_token: string
}

export interface LoginResponse {
    access_token: string
}

export interface InfoResponse {
    player: string,
    current_card: string
}

export interface ResultResponse {
    drawn_card: string,
    win: boolean,
    is_player_bankrupt: boolean,
    is_deck_empty: boolean
}