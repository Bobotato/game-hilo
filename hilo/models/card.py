from dataclasses import dataclass, field
from enum import Enum
from functools import total_ordering


class Ranks(Enum):
    A = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    J = 11
    Q = 12
    K = 13


class Suits(Enum):
    D = 1
    C = 2
    H = 3
    S = 4


RANKS = list(Ranks)
SUITS = list(Suits)


@total_ordering
@dataclass(frozen=True)
class Card:
    """Standard playing card class"""

    sort_index: int = field(repr=False)
    rank: Ranks
    suit: Suits

    @classmethod
    def create(cls, rank: Ranks, suit: Suits) -> "Card":
        return cls(cls.__calculate_sort_index(rank, suit), rank, suit)

    @staticmethod
    def __calculate_sort_index(rank: Ranks, suit: Suits) -> int:
        return RANKS.index(rank) * len(SUITS) + SUITS.index(suit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return self.sort_index == other.sort_index

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return self.sort_index > other.sort_index

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return self.sort_index < other.sort_index

    def __str__(self) -> str:
        return f"{self.rank.name} of {self.suit.name}"
