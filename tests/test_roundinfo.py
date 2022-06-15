import pytest

from hilo.models.card import Card
from hilo.models.player import Player
from hilo.models.roundinfo import RoundInfo


def test_roundinfo_init():
    player = Player("dummy")
    roundinfo = RoundInfo(player=player, current_card=Card("A", "H"))
    assert roundinfo.player == player
    assert roundinfo.current_card == Card("A", "H")


def test_current_card_getter():
    roundinfo = RoundInfo(player=Player("dummy"), current_card=Card("A", "H"))
    assert roundinfo.current_card == Card("A", "H")


def test_current_card_setter():
    roundinfo = RoundInfo(player=Player("dummy"), current_card=Card("A", "H"))
    roundinfo.current_card = Card("2", "H")
    assert roundinfo.current_card == Card("2", "H")


def test_current_card_setter_invalid_card_return_TypeError():
    roundinfo = RoundInfo(player=Player("dummy"), current_card=Card("A", "H"))
    with pytest.raises(TypeError):
        roundinfo.current_card = "test"


def test_player_getter():
    player = Player("dummy")
    roundinfo = RoundInfo(player=player, current_card=Card("A", "H"))
    assert roundinfo.player == player


def test_player_setter():
    player = Player("dummy")
    roundinfo = RoundInfo(player=player, current_card=Card("A", "H"))
    player2 = Player("dummy2")
    roundinfo.player = player2
    assert roundinfo.player == player2


def test_player_setter_invalid_player_return_TypeError():
    roundinfo = RoundInfo(player=Player("dummy"), current_card=Card("A", "H"))
    with pytest.raises(TypeError):
        roundinfo.player = "test"
