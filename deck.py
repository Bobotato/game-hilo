from random import shuffle
import card


class Deck:
    """Deck consisting of playing cards, starts with 52 playing cards"""
    def __init__(self, fill=False):
        if fill:
            self.fill()
        elif not fill:
            self._cards = []
        else:
            raise ValueError("Please use True or False to choose"
                             "if the deck starts with 52 cards.")

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def count(self):
        return len(self.cards)

    def deal(self, face):
        if self.count() == 0:
            raise ValueError("The deck's empty, no cards can "
                             "be dealt until refilled.")
        else:
            if face == "up":
                faceup_card = self.cards.pop()
                print(f"The face-up card is {faceup_card}")
                return faceup_card
            elif face == "down":
                facedown_card = self.cards.pop()
                print("The face-down card has been dealt.")
                return facedown_card
            else:
                raise ValueError("Cards can only be dealt "
                                 "face 'up' or 'down'")

    def fill(self):
        suits = card.suits
        values = card.values
        self.cards = [card.Card(value, suit) for suit in
                      SUITS for value in VALUES]
        return self.cards

    def shuffle(self):
        shuffle(self.cards)
        return self.cards

    def __repr__(self):
        return f"Deck of {self.count()} cards"
