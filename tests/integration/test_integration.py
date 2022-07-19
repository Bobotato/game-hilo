from random import seed

import pytest

from hilo.game import Game, Prediction
from hilo.models.card import Card


@pytest.mark.integtest
def test_compute_round_result_can_compute_after_start_round():
    seed(1)
    game = Game("test")
    game.start_round()
    round_result = game.compute_round_result(
        prediction=Prediction.HIGHER, bet=50
    )
    assert round_result.drawn_card == Card("J", "H")
    assert round_result.win
    assert not round_result.is_player_bankrupt
    assert not round_result.is_deck_empty


@pytest.mark.integtest
def test_compute_round_result_can_compute_over_multiple_rounds():
    seed(1)
    game = Game("test")
    game.start_round()
    round_result = game.compute_round_result(
        prediction=Prediction.HIGHER, bet=50
    )

    game.start_round()
    round_result = game.compute_round_result(
        prediction=Prediction.LOWER, bet=50
    )
    assert round_result.drawn_card == Card("10", "S")
    assert round_result.win
    assert not round_result.is_player_bankrupt
    assert not round_result.is_deck_empty


@pytest.mark.integtest
def test_compute_round_result_can_compute_consecutively():
    seed(1)
    game = Game("test")
    game.start_round()
    round_result = game.compute_round_result(
        prediction=Prediction.LOWER, bet=10
    )
    round_result = game.compute_round_result(
        prediction=Prediction.LOWER, bet=10
    )
    assert round_result.drawn_card == Card("10", "S")
    assert round_result.win
    assert not round_result.is_player_bankrupt
    assert not round_result.is_deck_empty


@pytest.mark.integtest
def test_deck_pops_correctly_over_multiple_start_round_and_compute_round_result(  # noqa: E501
    seeded_deck,
):
    seed(1)
    game = Game("test")
    game.start_round()
    assert game.deck.cards == seeded_deck[0:-1]

    game.compute_round_result(prediction=Prediction.HIGHER, bet=10)
    assert game.deck.cards == seeded_deck[0:-2]

    game.start_round()
    assert game.deck.cards == seeded_deck[0:-2]

    game.compute_round_result(prediction=Prediction.HIGHER, bet=10)
    assert game.deck.cards == seeded_deck[0:-3]


@pytest.mark.integtest
def test_player_credits_change_correctly_over_multiple_start_rounds_and_compute_round_results():  # noqa: E501
    seed(1)
    game = Game("test")
    assert game.player.credits == 100
    game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=100)
    assert game.player.credits == 200

    game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=50)
    assert game.player.credits == 150


@pytest.mark.integtest
def test_start_round_can_be_called_consecutively():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    round_info = game.start_round()
    assert round_info.player.name == "test"
    assert round_info.current_card == Card("9", "D")


@pytest.mark.integtest
def test_start_round_can_be_called_after_compute_round_result_if_also_called_beforehand():  # noqa: E501
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=50)

    round_info = game.start_round()
    assert round_info.player.name == "test"
    assert round_info.current_card == Card("J", "H")


@pytest.mark.integtest
def test_start_round_called_after_compute_round_result_raises_typeError_if_not_called_beforehand():  # noqa: E501
    seed(1)
    game = Game("test")
    with pytest.raises(TypeError):
        game.compute_round_result(prediction=Prediction.LOWER, bet=100)
        game.start_round()
