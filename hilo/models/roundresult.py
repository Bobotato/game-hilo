from dataclasses import KW_ONLY, dataclass

from .card import Card


@dataclass
class RoundResult:
    """This class holds the result of the round"""

    drawn_card: Card
    win: bool
    _: KW_ONLY
    is_player_bankrupt: bool
    is_deck_empty: bool
