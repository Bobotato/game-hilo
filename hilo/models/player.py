class Player:
    """A class to represent a player and their credits"""

    def __init__(self, name: str, credits: int = 100) -> None:
        self.name = name
        self.credits = credits

    @property
    def credits(self) -> int:
        return self._credits

    @credits.setter
    def credits(self, credits: int) -> None:
        if credits < 0:
            raise ValueError("Player can't have negative credits.")

        self._credits = credits

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("Player name cannot be blank.")

        self._name = name

    def is_bankrupt(self) -> bool:
        """Checks if player is bankrupt"""
        return self.credits <= 0

    def __repr__(self) -> str:
        return f"{self.name} with {self.credits} credits."
