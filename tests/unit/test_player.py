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


def test_is_player_bankrupt():
    player = Player(name="dummy", credits=0)
    assert player.credits == 0
    assert player.is_bankrupt()


def test_is_player_not_bankrupt():
    player = Player(name="dummy", credits=100)
    assert player.credits == 100
    assert not player.is_bankrupt()
