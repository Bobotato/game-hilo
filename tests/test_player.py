from hilo.models.player import Player


def test_player_init_name():
    dummy_player = Player(name="dummy", credits=100)
    assert dummy_player.name == "dummy"


def test_player_init_credits():
    dummy_player = Player(name="dummy", credits=200)
    assert dummy_player.credits == 200


def test_credits_getter():
    dummy_player = Player(name="dummy", credits=100)
    assert dummy_player.credits == 100


def test_credits_setter():
    dummy_player = Player(name="dummy", credits=100)
    dummy_player.credits = 200
    assert dummy_player.credits == 200


def test_name_getter():
    dummy_player = Player(name="dummy", credits=100)
    assert dummy_player.name == "dummy"


def test_name_setter():
    dummy_player = Player(name="dummy", credits=100)
    dummy_player.name = "notdummy"
    assert dummy_player.name == "notdummy"


def test_is_player_bankrupt():
    dummy_player = Player(name="dummy", credits=0)
    assert dummy_player.credits == 0
    assert dummy_player.is_bankrupt
