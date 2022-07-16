from random import seed

import pytest

import main
from hilo.game import Game, Prediction
from hilo.models.card import Card


@pytest.mark.integtest
def test_failed_round_bankruptcy_no_continue(monkeypatch, seeded_deck):
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

    monkeypatch.setattr("builtins.input", lambda _: "2")
    prediction = main.get_prediction(round_info)
    assert prediction == Prediction.LOWER
    monkeypatch.undo()

    monkeypatch.setattr("builtins.input", lambda _: 100)
    bet = main.get_bet(game)
    assert bet == 100
    monkeypatch.undo()

    round_result = game.compute_round_result(prediction=prediction, bet=bet)
    assert round_result.drawn_card == Card("J", "H")
    assert not round_result.win
    assert round_result.is_player_bankrupt
    assert not round_result.is_deck_empty
    assert game.player.credits == 0

    assert main.is_game_over(round_result)

    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert not main.is_restarting()
    with pytest.raises(SystemExit):
        main.end_game()
