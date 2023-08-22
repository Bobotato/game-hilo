import { Ranks } from '@/classes/PokerCard'
import { Suits } from '@/classes/PokerCard'
import { Card } from '@/classes/PokerCard'

export class Deck {
    cards: Array<Card>

    constructor(cards: Array<Card>) {
        this.cards = cards;
    }

    buildDeck() {
        for (let i = 0; i < Ranks.length; i++) {
            for (let x = 0; x < Ranks.length; x++) {
                let card = { Value: Ranks[x], Suit: Suits[i] };
                this.cards.push(card);
            }
        }
    }

    dealCard() {
        return this.cards.pop()
    }
}