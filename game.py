from deck import Deck
from player import Player


class Game:
    """This class includes all the methods required for the game of Hilo"""
    def __init__(self):
        self.d = Deck(populate = True)
        self.p = Player()
        self.faceup = None
        self.facedown = None

    def draw(self):
        return self.d.cards.pop()

    def take_bet(self, bet):
        if bet <= 0:
            raise ValueError("Bets cannot be 0 or negative.")
        elif bet > self.p.credits:
            raise ValueError("Bets cannot exceed player's credits.")
        self.p.credits -= bet

    def award_bet(self, bet):
        self.p.credits += (bet*2)

    def check_guess(self, guess):
        if guess == "higher":
            return self.faceup > self.facedown
        elif guess == "lower":
            return self.faceup < self.facedown
