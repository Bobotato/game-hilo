from card import Card
from player import Player


class Roundinfo:
    """This class holds the information for the current round"""
    def __init__(self, player, current_card):
        self.player = player
        self.current_card = current_card
    
    @property
    def current_card(self):
        return self._current_card

    @current_card.setter
    def current_card(self, current_card):
        if not isinstance(current_card, Card):
            raise ValueError("An invalid card was inserted "
                             "into the round info.")
        self._current_card = current_card

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise ValueError("An invalid player was inserted "
                             "into the round info.")
        self._player = player

