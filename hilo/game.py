from enum import Enum

from .models.deck import Deck
from .models.player import Player
from .models.roundinfo import RoundInfo
from .models.roundresult import RoundResult


class Prediction(Enum):
    HIGHER = 1
    LOWER = 2


class Game:
    """This class includes all the methods required for the game of Hilo"""

    def __init__(self, name):
        self.deck = Deck(populate=True, shuffle_deck=True)
        self.player = Player(name)
        self.__current_card = None

    def __award_bet(self, bet, *, multiplier=2):
        """
        Awards a bet to the player

        :param bet: The player's bet for the current round.
        :type bet: int
        :param multiplier: The multiple to multiply the bet by.
        :type multiplier: int
        """
        self.player.credits += bet * multiplier

    def compute_round_result(self, bet, prediction):
        """
        Takes the player's bet and prediction and computes the result of the round.

        :param bet: The player's bet for the current round.
        :type bet: int
        :param prediction: The player's prediction for the current round.
        :type prediction: Prediction
        :return: An instance of a RoundResult with drawn_card and the result
                 of the prediction.
        :rtype: RoundResult
        """
        self.__take_bet(bet)
        drawn_card = self.deck.draw_card()
        win = self.__is_win(drawn_card, prediction)

        if win:
            self.__award_bet(bet)

        result = RoundResult(
            drawn_card,
            win,
            is_player_bankrupt=self.player.is_bankrupt(),
            is_deck_empty=self.deck.is_empty(),
        )

        self.__current_card = drawn_card

        return result

    def __is_win(self, drawn_card, prediction):
        """
        Checks if the player won the round.

        :param drawn_card: The drawn card for the current round.
        :type drawn_card: Card
        :param prediction: The player's prediction for the current round.
        :type prediction: Prediction
        :return: True/False based whether the player's prediction is correct.
        :rtype: bool
        """
        match prediction:
            case Prediction.HIGHER:
                return drawn_card > self.__current_card
            case Prediction.LOWER:
                return drawn_card < self.__current_card
            case _:
                raise TypeError(
                    "prediction must be an instance of a Prediction"
                )

    def start_round(self):
        """Starts round, drawing current_card and returning
        an instance of Roundinfo"""
        if self.__current_card is None:
            self.__current_card = self.deck.draw_card()

        return RoundInfo(self.player, self.__current_card)

    def __take_bet(self, bet):
        """Takes the player's bet and removes it from their account"""
        if bet <= 0:
            raise ValueError("Bets cannot be 0 or negative.")
        elif bet > self.player.credits:
            raise ValueError("Bets cannot exceed player's credits.")

        self.player.credits -= bet
