from random import seed

import pytest

from hilo.game import Game, Prediction
from hilo.models.card import Card, Ranks, Suits
from hilo.models.player import Player
from hilo.models.roundinfo import RoundInfo
from hilo.models.roundresult import RoundResult


@pytest.mark.integtest
def test_can_play_single_round():
    seed(1)
    game = Game("test")
    game.start_round()
    round_result = game.compute_round_result(prediction=Prediction.HIGHER, bet=50)
    assert round_result == RoundResult(
        drawn_card=Card.create(Ranks.J, Suits.H),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )


@pytest.mark.integtest
def test_can_play_multiple_rounds():
    seed(1)
    game = Game("test")
    game.start_round()
    round_result = game.compute_round_result(prediction=Prediction.HIGHER, bet=50)

    game.start_round()
    round_result = game.compute_round_result(prediction=Prediction.LOWER, bet=50)
    assert round_result == RoundResult(
        drawn_card=Card.create(Ranks.TEN, Suits.S),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )


@pytest.mark.integtest
def test_can_play_subsequent_rounds_without_explicitly_starting_round():
    seed(1)
    game = Game("test")
    game.start_round()
    round_result = game.compute_round_result(prediction=Prediction.LOWER, bet=10)
    round_result = game.compute_round_result(prediction=Prediction.LOWER, bet=10)
    assert round_result == RoundResult(
        drawn_card=Card.create(Ranks.TEN, Suits.S),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )


@pytest.mark.integtest
def test_player_credits_changes_correctly_for_subsequent_round():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    assert round_info.player.credits == 100
    game.compute_round_result(prediction=Prediction.HIGHER, bet=100)

    game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=50)
    assert round_info.player.credits == 150


@pytest.mark.integtest
def test_can_start_round_again_without_playing():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    round_info = game.start_round()
    assert round_info == RoundInfo(
        player=Player(name="test"),
        current_card=Card.create(Ranks.NINE, Suits.D),
    )


@pytest.mark.integtest
def test_can_start_round_again_after_playing():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=50)

    round_info = game.start_round()
    assert round_info == RoundInfo(
        player=Player(name="test", credits=150),
        current_card=Card.create(Ranks.J, Suits.H),
    )


@pytest.mark.integtest
def test_cannot_play_first_round_without_starting_round_first():
    seed(1)
    game = Game("test")
    with pytest.raises(TypeError):
        game.compute_round_result(prediction=Prediction.LOWER, bet=100)
        game.start_round()
