from card import Card, SUITS, VALUES

class Deck:
    """Deck consisting of playing cards,
    use fill=True to create a 52 card deck on init"""
    def __init__(self, populate=False):
        if populate:
            self.populate()
        elif not populate:
            self._cards = []
        else:
            raise ValueError("Please use True or False to choose"
                             "if the deck starts with 52 cards.")

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def populate(self):
        self.cards = [Card(value, suit) for suit in
                      SUITS for value in VALUES]
        return self.cards

    def __repr__(self):
        return (f"A deck of {self.cards}")
