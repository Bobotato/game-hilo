from card import Card


class RoundResult:
    """This class holds the result of the round"""

    def __init__(self, drawn_card, win, *, is_player_bankrupt, is_deck_empty):
        self.drawn_card = drawn_card
        self.win = win
        self.is_player_bankrupt = is_player_bankrupt
        self.is_deck_empty = is_deck_empty

    @property
    def drawn_card(self):
        return self._drawn_card

    @drawn_card.setter
    def drawn_card(self, drawn_card):
        if not isinstance(drawn_card, Card):
            raise TypeError("drawn_card must be an instance of a Card")

        self._drawn_card = drawn_card

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, win):
        if not isinstance(win, bool):
            raise TypeError("win must be a boolean")

        self._win = win

    def __repr__(self):
        return f"{self.drawn_card}, {self.win}"
