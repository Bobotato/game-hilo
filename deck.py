from random import shuffle


suits = ["H", "D", "C", "S"]

values = ["A", "2", "3", "4", "5", "6", "7",
          "8", "9", "10", "J", "Q", "K"]


class Deck:
    """Deck consisting of playing cards, starts with 52 playing cards"""
    def __init__(self):
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def restore(self):
        self.cards = [Card(value, suit) for suit in suits for value in values]
        return self.cards

    def deal(self, face):
        if self.count() == 0:
            raise ValueError("The deck's empty, no cards can "
                             "be dealt until restored.")
        else:
            if face == "up":
                faceup_card = self.cards.pop()
                print(f"The face-up card is {faceup_card}")
                return faceup_card
            elif face == "down":
                facedown_card = self.cards.pop()
                print("The face-down card has been dealt.")
                return facedown_card

    def shuffle(self):
        shuffle(self.cards)
        return self.cards
