export enum Suits { "Spades", "Diamonds", "Clubs", "Hearts" };
export enum Ranks { "A", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "J", "Q", "K" };

export class Card {
    suit: Suits
    rank: Ranks

    constructor(suit: Suits, rank: Ranks) {
        this.suit = suit;
        this.rank = rank;
    }
}