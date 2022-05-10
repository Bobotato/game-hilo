from enum import Enum
from deck import Deck
from player import Player


class Predictions(Enum):
    HIGHER = 1
    LOWER = 0


class Game:
    """This class includes all the methods required for the game of Hilo"""
    def __init__(self):
        self.d = Deck(populate=True)
        self.p = Player()
        self.faceup = None
        self.facedown = None

    def award_bet(self, bet):
        """Awards double the bet to the player"""
        self.p.credits += (bet * 2)

    def check_prediction(self, current_card, drawn_card, prediction):
        """Checks the player's prediction and returns True/False"""
        if prediction == Predictions.HIGHER:
            return current_card > drawn_card
        elif prediction == Predictions.LOWER:
            return current_card < drawn_card
        else:
            raise ValueError("Guess must be either 'higher' or 'lower'.")

    def draw_card(self):
        """Draws a card from the deck"""
        return self.d.cards.pop()

    def take_bet(self, bet):
        """Takes the player's bet and removes it from their account"""
        if bet <= 0:
            raise ValueError("Bets cannot be 0 or negative.")
        elif bet > self.p.credits:
            raise ValueError("Bets cannot exceed player's credits.")
        self.p.credits -= bet

