from random import seed

import pytest

import main
from hilo.game import Game, Prediction
from hilo.models.card import Card


@pytest.mark.integtest
def test_successful_round_with_continue(monkeypatch, seeded_deck):
    monkeypatch.setattr("builtins.input", lambda _: "test")
    name = main.get_name()
    assert name == "test"
    monkeypatch.undo()

    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert main.is_playing()
    monkeypatch.undo()

    seed(1)
    game = Game(name)
    assert game.deck.cards == seeded_deck
    assert game.player.name == "test"
    assert game.player.credits == 100
    assert game._Game__current_card is None

    round_info = game.start_round()
    assert round_info.player.name == "test"

    monkeypatch.setattr("builtins.input", lambda _: "1")
    prediction = main.get_prediction(round_info)
    assert prediction == Prediction.HIGHER
    monkeypatch.undo()

    monkeypatch.setattr("builtins.input", lambda _: 50)
    bet = main.get_bet(game)
    assert bet == 50
    monkeypatch.undo()

    round_result = game.compute_round_result(
        prediction=Prediction.HIGHER, bet=bet
    )
    assert round_result.drawn_card == Card("J", "H")
    assert round_result.win
    assert not round_result.is_player_bankrupt
    assert not round_result.is_deck_empty
    assert game.player.credits == 150

    assert not main.is_game_over(round_result)

    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert main.is_continuing()

    assert game.deck.cards == seeded_deck[0:-2]
    assert game.player.name == "test"
    assert game.player.credits == 150
    assert game._Game__current_card == Card("J", "H")

    round_info = game.start_round()
    assert round_info.player.name == "test"

    monkeypatch.setattr("builtins.input", lambda _: "2")
    prediction = main.get_prediction(round_info)
    assert prediction == Prediction.LOWER
    monkeypatch.undo()

    monkeypatch.setattr("builtins.input", lambda _: 50)
    bet = main.get_bet(game)
    assert bet == 50
    monkeypatch.undo()

    round_result = game.compute_round_result(
        prediction=Prediction.LOWER, bet=bet
    )
    assert round_result.drawn_card == Card("10", "S")
    assert round_result.win
    assert not round_result.is_player_bankrupt
    assert not round_result.is_deck_empty
    assert game.player.credits == 200

    assert not main.is_game_over(round_result)

    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert not main.is_continuing()
    with pytest.raises(SystemExit):
        main.end_game()
