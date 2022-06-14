import pytest

from hilo.models.player import Player


def test_player_init_name():
    player = Player(name="dummy", credits=100)
    assert player.name == "dummy"


def test_player_init_credits():
    player = Player(name="dummy", credits=200)
    assert player.credits == 200


def test_player_init_credits_default():
    player = Player(name="dummy")
    assert player.credits == 100


def test_credits_getter():
    player = Player(name="dummy", credits=100)
    assert player.credits == 100


def test_credits_setter():
    player = Player(name="dummy", credits=100)
    player.credits = 200
    assert player.credits == 200


def test_credits_setter_negative_credit_raise_ValueError():
    with pytest.raises(ValueError):
        Player(name="dummy", credits=-100)


def test_name_getter():
    player = Player(name="dummy", credits=100)
    assert player.name == "dummy"


def test_name_setter():
    player = Player(name="dummy", credits=100)
    player.name = "notdummy"
    assert player.name == "notdummy"


def test_name_setter_invalid_name_raise_ValueError():
    with pytest.raises(ValueError):
        Player(name="", credits=100)


def test_is_player_bankrupt():
    player = Player(name="dummy", credits=0)
    assert player.credits == 0
    assert player.is_bankrupt()


def test_is_player_not_bankrupt():
    player = Player(name="dummy", credits=100)
    assert player.credits == 100
    assert not player.is_bankrupt()


def test_player_repr():
    player = Player(name="dummy", credits=100)
    assert repr(player) == "dummy with 100 credits."
