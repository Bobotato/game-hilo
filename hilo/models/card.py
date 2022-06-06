from functools import total_ordering

VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["D", "C", "H", "S"]


@total_ordering
class Card:
    """Standard Playing Card Class"""

    def __init__(self, value: str, suit: str) -> None:
        self.value = value
        self.suit = suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit not in SUITS:
            raise ValueError(
                "Suit must be a part of the 4 French suits."
                "(H for Hearts, D for Diamonds...)"
            )
        self._suit = suit

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value not in VALUES:
            raise ValueError(
                "Value must be a part of the 13 values "
                "in a standard deck of cards. (A, 2, 3..)"
            )
        self._value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return (VALUES.index(self.value), SUITS.index(self.suit)) == (
            (VALUES.index(other.value), SUITS.index(other.suit))
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return (VALUES.index(self.value), SUITS.index(self.suit)) < (
            (VALUES.index(other.value), SUITS.index(other.suit))
        )

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return (VALUES.index(self.value), SUITS.index(self.suit)) > (
            (VALUES.index(other.value), SUITS.index(other.suit))
        )

    def __repr__(self) -> str:
        return f"{self.value}{self.suit}"
