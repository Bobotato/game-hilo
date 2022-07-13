from random import seed

import pytest

from hilo.game import Game, Prediction
from hilo.models.card import Card


def test_game_init(seeded_deck):
    seed(1)
    game = Game("test")
    assert game.deck.cards == seeded_deck
    assert game.player.name == "test"
    assert game._Game__current_card is None


def test_award_bet():
    game = Game("test")
    assert game.player.credits == 100

    game._Game__award_bet(bet=100, multiplier=5)
    assert game.player.credits == 600


def test_award_bet_multiplier_default():
    game = Game("test")
    assert game.player.credits == 100

    game._Game__award_bet(bet=100)
    assert game.player.credits == 300


def test_compute_round_result():
    seed(1)
    game = Game("test")
    assert game.player.credits == 100

    game.start_round()
    assert game._Game__current_card == Card("9", "D")

    result = game.compute_round_result(bet=100, prediction=Prediction.HIGHER)
    assert result.drawn_card == Card("J", "H")
    assert result.win
    assert not result.is_player_bankrupt
    assert not result.is_deck_empty
    assert game._Game__current_card == Card("J", "H")
    assert game.player.credits == 200


def test_is_win_prediction_higher():
    game = Game("test")
    game._Game__current_card = Card("A", "H")
    assert game._Game__is_win(
        drawn_card=Card("5", "H"), prediction=Prediction.HIGHER
    )


def test_is_win_prediction_lower():
    game = Game("test")
    game._Game__current_card = Card("5", "H")
    assert game._Game__is_win(
        drawn_card=Card("A", "H"), prediction=Prediction.LOWER
    )


def test_is_win_invalid_prediction_raise_TypeError():
    game = Game("test")
    game._Game__current_card = Card("5", "H")
    with pytest.raises(TypeError):
        game._Game__is_win(drawn_card=Card("A", "H"), prediction="test")


def test_start_round():
    game = Game("test")
    game._Game__current_card = Card("A", "H")

    roundinfo = game.start_round()
    assert roundinfo.player.name == "test"
    assert roundinfo.current_card == Card("A", "H")


def test_start_round_no_current_card():
    seed(1)
    game = Game("test")
    assert game._Game__current_card is None

    roundinfo = game.start_round()
    assert roundinfo.player.name == "test"
    assert game._Game__current_card == Card("9", "D")
    assert roundinfo.current_card == Card("9", "D")


def test_take_bet():
    game = Game("test")
    assert game.player.credits == 100

    game._Game__take_bet(bet=100)
    assert game.player.credits == 0


def test_take_bet_insufficient_credits_raise_ValueError():
    game = Game("test")
    assert game.player.credits == 100

    with pytest.raises(ValueError):
        game._Game__take_bet(bet=1000)


def test_take_bet_less_than_zero_bet_raise_ValueError():
    game = Game("test")
    assert game.player.credits == 100

    with pytest.raises(ValueError):
        game._Game__take_bet(bet=-100)
