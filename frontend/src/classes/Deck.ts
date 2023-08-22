import { CardRanks } from '@/classes/PokerCard'
import { CardSuits } from '@/classes/PokerCard'
import { Card } from '@/classes/PokerCard'

export class Deck {
    cards: Array<Card>

    constructor(cards: Array<Card>, buildDeck: boolean) {
        this.cards = cards

        if (buildDeck) {
            this.refreshDeck()
        }
    }

    refreshDeck() {
        for (let i = 0; i < CardRanks.length; i++) {
            for (let j = 0; j < CardSuits.length; j++) {
                const card = new Card(CardSuits[i], CardRanks[j]);
                this.cards.push(card);
            }
        }
    }

    dealCard() {
        return this.cards.pop()
    }
}