export const CardRanks = ["A", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "J", "Q", "K"] as const;
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
}