class Player:
    '''A class to represent a player and their credits'''
    def __init__(self, credits=100):
        self.credits = credits

    @property
    def credits(self):
        return self._credits

    @money.setter
    def credits(self, credits):
        if credits < 0:
            raise ValueError("Player can't have negative credits.")
        self._credits = credits

    def __repr__(self):
        return f"A player with {self.credits} credits."

