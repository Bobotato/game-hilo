from card import Card
from enum import Enum
from deck import Deck
from player import Player
from random import shuffle
from roundinfo import RoundInfo
from roundresult import RoundResult


class Predictions(Enum):
    HIGHER = 1
    LOWER = 0


class Game:
    """This class includes all the methods required for the game of Hilo"""
    def __init__(self, name):
        self.d = Deck(populate=True)
        self.p = Player(name)
        self.current_card = None

    @property
    def current_card(self):
        return self.__current_card

    @current_card.setter
    def current_card(self, current_card):
        if not isinstance(current_card, Card):
            raise ValueError("current_card must be an instance of a Card.")
        self.__current_card = current_card

    def award_bet(self, bet):
        """Awards double the bet to the player"""
        self.p.credits += (bet * 2)

    def check_bankrupt(self):
        """
        Checks if self.p.credits is 0, returns True if player is bankrupt.

        :return: 'True' if self.p.credits is 0
        :rtype: bool
        """
        if self.p.credits == 0:
            return True

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

    def end_round(self, bet, prediction):
        """Takes bet, prediction from the user, draws a card, checks prediction
        and returns an instance of Roundresult with the result"""
        drawn_card = self.draw_card()
        if prediction == "1":
            result = self.check_prediction(roundinfo.current_card,
                                           drawn_card, Predictions.HIGHER)
        elif prediction == "2":
            result = self.check_prediction(roundinfo.current_card,
                                           drawn_card, Predictions.LOWER)
        if result:
            self.award_bet(bet)
        return RoundResult(drawn_card, result)

    def start_round(self):
        """Starts round by shuffling deck, drawing current_card and returning
        an instance of Roundinfo"""
        shuffle(self.d.cards)
        current_card = self.draw_card()
        return RoundInfo(self.p, self.current_card)

    def swap_cards(self):
        """Sets the drawn_card to be current_card"""
        roundinfo.current_card = roundresult.drawn_card

    def take_bet(self, bet):
        """Takes the player's bet and removes it from their account"""
        if bet <= 0:
            raise ValueError("Bets cannot be 0 or negative.")
        elif bet > self.p.credits:
            raise ValueError("Bets cannot exceed player's credits.")
        self.p.credits -= bet

