from random import shuffle
from typing import List

from .card import SUITS, VALUES, Card


class Deck:
    """
    Deck consisting of playing cards,
    use populate=True to create a 52 card deck,
    or shuffle=True to shuffle the deck on init.
    """

    def __init__(
        self, populate: bool = False, shuffle_deck: bool = False
    ) -> None:
        self.cards = []

        if populate:
            self.cards = Deck.generate_full_deck()

        if shuffle_deck:
            shuffle(self.cards)

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @cards.setter
    def cards(self, cards: List[Card]) -> None:
        for card in cards:
            if not isinstance(card, Card):
                raise ValueError("You have tried to insert an invalid card.")

        self._cards = cards

    def draw_card(self) -> Card:
        """Draws a card from the deck"""
        return self.cards.pop()

    @staticmethod
    def generate_full_deck() -> List[Card]:
        """Generates a list of 52 cards"""
        return [Card(value, suit) for suit in SUITS for value in VALUES]

    def is_empty(self) -> bool:
        "Checks if deck is empty" ""
        return len(self.cards) == 0

    def __repr__(self) -> str:
        return str(self.cards)
