from dataclasses import dataclass


@dataclass
class Player:
    """A class to represent a player and their credits"""

    name: str
    credits: int = 100

    def is_bankrupt(self) -> bool:
        """Checks if player is bankrupt"""
        return self.credits <= 0
