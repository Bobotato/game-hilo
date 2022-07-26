from hilo.models.card import Card, Ranks, Suits
from hilo.models.player import Player
from hilo.models.roundinfo import RoundInfo


def test_roundinfo_init():
    player = Player("dummy")
    roundinfo = RoundInfo(
        player=player, current_card=Card.create(Ranks.A, Suits.H)
    )
    assert roundinfo == RoundInfo(
        player=player, current_card=Card.create(Ranks.A, Suits.H)
    )
