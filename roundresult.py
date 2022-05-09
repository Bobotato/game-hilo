from card import Card


class Roundresult:
    """This class holds the result of the round"""
    def __init__(self, drawn_card, win):
        self.drawn_card = drawn_card
        self.win = win

    @property
    def drawn_card(self):
        return self._drawn_card

    @drawn_card.setter
    def drawn_card(self, drawn_card):
        if not isinstance(drawn_card, Card):
            raise TypeError("drawn_card must be an "
                            "instance of Card")
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
        return ("Drawn card = " + str(self.drawn_card) + ", Won? = " + str(self.win))
