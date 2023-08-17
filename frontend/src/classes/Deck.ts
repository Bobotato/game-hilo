import { RANKS } from '@/classes/PokerCard'
import { SUITS } from '@/classes/PokerCard'
import { Card } from '@/classes/PokerCard'

export class Deck {
    cards: Array<Card>

    constructor(cards: Array<Card>) {
        this.cards = cards;
    }
}

function getDeck() {
    let deck = new Array();

    for (let i = 0; i < SUITS.length; i++) {
        for (let x = 0; x < RANKS.length; x++) {
            let card = { Value: RANKS[x], Suit: suits[i] };
            deck.push(card);
        }
    }

    return deck;
}

function dealCard(deck) {
    return deck.pop();
}