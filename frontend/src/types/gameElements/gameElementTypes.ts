export interface Card {
    sort_index: number,
    rank: number,
    suit: number
}

export interface Player {
    name: string,
    credits: number
}

export interface Prediction {
    prediction: number
}

export interface RoundInfo {
    player: Player,
    current_card: Card
}

export interface RoundResult {
    drawn_card: Card,
    win: boolean
    is_player_bankrupt: boolean
    is_deck_empty: boolean
}