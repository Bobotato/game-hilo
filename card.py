VALUES = ["A", "2", "3", "4", "5", "6", "7",
          "8", "9", "10", "J", "Q", "K"]
SUITS = ["D", "C", "H", "S"]


class Card:
    """Standard Playing Card Class"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def suit(self, suit):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit not in SUITS:
            raise ValueError("Suit must be a part of the 4 French suits."
                             "(H for Hearts, D for Diamonds...)")
        self._suit = suit

    @property
    def value(self, value):
        return self._value

    @value.setter
    def value(self, value):
        if value not in VALUES:
            raise ValueError("Value must be a part of the 13 values "
                             "in a standard deck of cards. (A, 2, 3..)")
        self._value = value

    def __repr__(self):
        return (f"{self.value}{self.suit}") 
