from enum import Enum
from random import shuffle

from card import Card
from deck import Deck
from player import Player
from roundinfo import RoundInfo
from roundresult import RoundResult


class Predictions(Enum):
    HIGHER = 1
    LOWER = 0


class Game:
    """This class includes all the methods required for the game of Hilo"""
    def __init__(self, name):
        self.deck = Deck(populate=True)
        self.player = Player(name)

    def award_bet(self, bet, multiplier=2):
        """Awards double the bet to the player"""
        self.player.credits += (bet * multiplier)

    def check_prediction(self, drawn_card, prediction):
        """
        Checks the player's prediction and returns True/False

        :param drawn_card: The drawn card for the current round.
        :type drawn_card: Card
        :param prediction: The player's prediction for the current round.
        :type prediction: str
        :return: True/False based whether the player's prediction is correct.
        :rtype: bool

        """
        if prediction == Predictions.HIGHER:
            return drawn_card > self.current_card
        elif prediction == Predictions.LOWER:
            return drawn_card < self.current_card
        else:
            raise ValueError("Guess must be either 'higher' or 'lower'.")

    def compute_roundresult(self, bet, prediction):
        """
        Computes the result of a round with a given bet and prediction,
        and returns an instance of Roundresult with the result.

        :param bet: The player's bet for the current round.
        :type bet: int
        :param prediction: The player's prediction for the current round.
        :type prediction: str
        :return: An instance of a RoundResult with drawn_card and the result
                 of the prediction.
        :rtype: RoundResult
        """
        drawn_card = self.draw_card()
        if prediction == "1":
            result = self.check_prediction(drawn_card, Predictions.HIGHER)
        elif prediction == "2":
            result = self.check_prediction(drawn_card, Predictions.LOWER)
        if result:
            self.award_bet(bet)
        roundresult = RoundResult(drawn_card, result)
        self.swap_cards(drawn_card)
        return roundresult

    def start_round(self):
        """Starts round by shuffling deck, drawing current_card and returning
        an instance of Roundinfo"""
        shuffle(self.deck.cards)
        self.current_card = self.draw_card()
        return RoundInfo(self.player, self.current_card)

    def swap_cards(self, drawn_card):
        """
        Sets a drawn card to be the current card.
        
        :param drawn_card: An instance of a Card.
        :type drawn_card: Card
        """
        self.current_card = drawn_card

    def take_bet(self, bet):
        """Takes the player's bet and removes it from their account"""
        if bet <= 0:
            raise ValueError("Bets cannot be 0 or negative.")
        elif bet > self.player.credits:
            raise ValueError("Bets cannot exceed player's credits.")
        self.player.credits -= bet

    def update_roundinfo(self):
        """
        Returns an instance of RoundInfo with the latest player and
        current card
        
        :return: An instance of a RoundInfo
        :rtype: RoundInfo
        """
        return RoundInfo(self.player, self.current_card)
