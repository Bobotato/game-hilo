export const SUITS = ["spades", "diamonds", "clubs", "hearts"];
export const RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];


export class Card {
    suit: string
    rank: string

    constructor(suit: string, rank: string) {
        if (!SUITS.includes(suit)) {
            throw new Error("Invalid suit");
        }
        if (!RANKS.includes(rank)) {
            throw new Error("Invalid rank");
        }

        this.suit = suit;
        this.rank = rank;
    }
}