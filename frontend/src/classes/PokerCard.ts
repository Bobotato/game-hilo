export const CardRanks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] as const;
export type Ranks = typeof CardRanks[number]

export const CardSuits = ["Spades", "Diamonds", "Clubs", "Hearts"] as const;
export type Suits = typeof CardSuits[number]

export class Card {
    suit: Suits
    rank: Ranks

    constructor(suit: Suits, rank: Ranks) {
        this.suit = suit;
        this.rank = rank;
    }

    toString() {
        return `${this.rank} of ${this.suit}`
    }
}