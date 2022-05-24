class Player:
    """A class to represent a player and their credits"""

    def __init__(self, name, credits=100):
        self.name = name
        self.credits = credits

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits):
        if credits < 0:
            raise ValueError("Player can't have negative credits.")

        self._credits = credits

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Player name cannot be blank.")

        self._name = name

    def is_bankrupt(self):
        """Checks if player is bankrupt"""
        return self.credits == 0

    def __repr__(self):
        return f"{self.name} with {self.credits} credits."
