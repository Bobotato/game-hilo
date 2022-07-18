from random import seed

import pytest

from hilo.game import Game, Prediction
from hilo.models.card import Card


@pytest.mark.integtest
def test_start_round_gets_player_and_current_card():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    assert round_info.player.name == "test"
    assert round_info.current_card == Card("9", "D")


@pytest.mark.integtest
def test_start_round_gets_player_and_current_card_over_multiple_rounds():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    round_result = game.compute_round_result(
        prediction=Prediction.HIGHER, bet=50
    )
    assert round_result.drawn_card == Card("J", "H")

    round_info = game.start_round()
    assert round_info.player.name == "test"
    assert round_info.current_card == Card("J", "H")


@pytest.mark.integtest
def test_start_round_gets_player_and_current_card_after_restart():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    game.compute_round_result(prediction=Prediction.LOWER, bet=100)

    seed(1)
    game = Game("test")
    round_info = game.start_round()
    assert round_info.player.name == "test"
    assert round_info.current_card == Card("J", "H")


@pytest.mark.integtest
def test_compute_round_result_after_start_round():
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
def test_compute_round_result_computes_over_multiple_rounds():
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
def test_compute_round_result_computes_after_restart():
    seed(1)
    game = Game("test")
    round_info = game.start_round()
    round_result = game.compute_round_result(
        prediction=Prediction.LOWER, bet=100
    )

    seed(1)
    game = Game("test")
    round_info = game.start_round()
    assert round_info.current_card == Card("9", "D")
    round_result = game.compute_round_result(
        prediction=Prediction.LOWER, bet=50
    )
    assert round_result.drawn_card == Card("J", "H")
    assert not round_result.win
    assert not round_result.is_player_bankrupt
    assert not round_result.is_deck_empty


@pytest.mark.integtest
def test_deck_resets_after_restart(seeded_deck):
    seed(1)
    game = Game("test")
    game.start_round()
    game.compute_round_result(prediction=Prediction.LOWER, bet=100)

    seed(1)
    game = Game("test")
    assert game.deck.cards == seeded_deck


@pytest.mark.integtest
def test_deck_pops_correctly_over_multiple_rounds(seeded_deck):
    seed(1)
    game = Game("test")
    game.start_round()
    assert game.deck.cards == seeded_deck[0:-1]

    game.compute_round_result(prediction=Prediction.HIGHER, bet=10)
    assert game.deck.cards == seeded_deck[0:-2]

    game.start_round()
    assert game.deck.cards == seeded_deck[0:-3]

    game.compute_round_result(prediction=Prediction.HIGHER, bet=10)
    assert game.deck.cards == seeded_deck[0:-4]


@pytest.mark.integtest
def test_player_credits_back_to_default_after_restart():
    game = Game("test")
    assert game.player.credits == 100
    game.player.credits = 0
    game = Game("test")
    assert game.player.credits == 100


@pytest.mark.integtest
def test_player_credits_change_correctly_over_multiple_rounds():
    seed(1)
    game = Game("test")
    assert game.player.credits == 100
    game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=100)
    assert game.player.credits == 200

    game.start_round()
    game.compute_round_result(prediction=Prediction.HIGHER, bet=50)
    assert game.player.credits == 150
