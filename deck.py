from random import shuffle

from card import Card, SUITS, VALUES


class Deck:
    """
    Deck consisting of playing cards,
    use populate=True to create a 52 card deck,
    or shuffle=True to shuffle the deck on init.
    """
    def __init__(self, populate=False, shuffle=False):
        self.cards = []
        if populate:
            self.populate()
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        for card in cards:
            if not isinstance(card, Card):
                raise ValueError("You have tried to insert"
                                 "an invalid card.")
        self._cards = cards

    def populate(self):
        self.cards = ([Card(value, suit) for suit in
                      SUITS for value in VALUES])

    def shuffle(self):
        """Shuffles the deck"""
        shuffle(self.cards)

    def __repr__(self):
        return str(self.cards)

