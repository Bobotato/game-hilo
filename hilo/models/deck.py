from dataclasses import dataclass, field
from random import shuffle
from typing import List

from .card import Card, Ranks, Suits


@dataclass
class Deck:
    """
    Deck consisting of playing cards
    """

    cards: List[Card] = field(default_factory=lambda: [])
    populate: bool = False
    shuffle_deck: bool = False

    def __post_init__(self):
        if self.populate:
            self.cards = Deck.generate_full_deck()

        if self.shuffle_deck:
            shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draws a card from the deck"""
        return self.cards.pop()

    @staticmethod
    def generate_full_deck() -> List[Card]:
        """Generates a list of 52 cards"""
        return [Card.create(rank, suit) for suit in Suits for rank in Ranks]

    def is_empty(self) -> bool:
        """Checks if deck is empty"""
        return len(self.cards) == 0
