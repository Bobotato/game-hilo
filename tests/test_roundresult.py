import pytest

from hilo.models.roundresult import Card, RoundResult


def test_round_result_init():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=True,
        is_deck_empty=True,
    )
    assert roundresult.drawn_card == Card("A", "H")
    assert roundresult.win
    assert roundresult.is_player_bankrupt
    assert roundresult.is_deck_empty


def test_drawn_card_getter():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    assert roundresult.drawn_card == Card("A", "H")


def test_drawn_card_setter():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    roundresult.drawn_card = Card("2", "H")
    assert roundresult.drawn_card == Card("2", "H")


def test_drawn_card_setter_invalid_card_return_TypeError():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    with pytest.raises(TypeError):
        roundresult.drawn_card = "test"


def test_win_getter():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    assert roundresult.win


def test_win_setter():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    roundresult.win = False
    assert not roundresult.win


def test_win_setter_invalid_win_return_TypeError():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    with pytest.raises(TypeError):
        roundresult.win = "test"


def test_roundresult_repr():
    roundresult = RoundResult(
        drawn_card=Card("A", "H"),
        win=True,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    assert repr(roundresult) == "AH, True"
