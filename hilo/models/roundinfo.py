from .card import Card
from .player import Player


class RoundInfo:
    """This class holds the information for the current round"""

    def __init__(self, player: Player, current_card: Card):
        self.player = player
        self.current_card = current_card

    @property
    def current_card(self) -> Card:
        return self._current_card

    @current_card.setter
    def current_card(self, current_card: Card) -> None:
        if not isinstance(current_card, Card):
            raise TypeError("current_card must be an instance of a Card")

        self._current_card = current_card

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError("player must be an instance of a Player")

        self._player = player
