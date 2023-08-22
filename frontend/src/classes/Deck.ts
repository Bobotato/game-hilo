import { CardRanks } from '@/classes/PokerCard'
import { CardSuits } from '@/classes/PokerCard'
import { Card } from '@/classes/PokerCard'

export class Deck {
    cards: Array<Card>

    constructor(buildDeck: boolean, shuffleDeck: boolean) {
        this.cards = []

        if (buildDeck) {
            this.refreshDeck()
        }
        if (shuffleDeck) {
            this.shuffleDeck()
        }
    }

    toString() {
        return `${this.cards}`
    }

    refreshDeck() {
        for (let i = 0; i < CardSuits.length; i++) {
            for (let j = 0; j < CardRanks.length; j++) {
                const card = new Card(CardSuits[i], CardRanks[j]);
                this.cards.push(card);
            }
        }
    }

    shuffleDeck() {
        for (let i = this.cards.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            const temp = this.cards[i];
            this.cards[i] = this.cards[j];
            this.cards[j] = temp;
        }
    }

    dealCard() {
        return this.cards.pop()
    }
}