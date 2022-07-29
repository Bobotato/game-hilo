from dataclasses import dataclass

from .card import Card
from .player import Player


@dataclass
class RoundInfo:
    """This class holds the information for the current round"""

    player: Player
    current_card: Card
