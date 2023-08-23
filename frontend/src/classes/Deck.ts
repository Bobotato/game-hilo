import { CardRanks } from '@/classes/PokerCard'
import { CardSuits } from '@/classes/PokerCard'
import { Card } from '@/classes/PokerCard'

export class Deck {
    cards: Array<Card>

    constructor(populateDeck: boolean, shuffleDeck: boolean) {
        this.cards = []

        if (populateDeck) {
            this.generateDeck()
        }
        if (shuffleDeck) {
            this.shuffleDeck()
        }
    }

    toString() {
        return `${this.cards}`
    }

    generateDeck() {
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

    dealCard(): Card | undefined {
         if (!this.isEmpty()) {
            const card = this.cards.pop()
            if (card instanceof Card) {
                return card
            }
        }
    }

    isEmpty(): boolean {
        return this.cards.length === 0
    }
}
