from hilo.models.card import Card, Ranks, Suits
from hilo.models.roundresult import RoundResult


def test_round_result_init():
    roundresult = RoundResult(
        drawn_card=Card.create(Ranks.A, Suits.H),
        win=False,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
    assert roundresult == RoundResult(
        drawn_card=Card.create(Ranks.A, Suits.H),
        win=False,
        is_player_bankrupt=False,
        is_deck_empty=False,
    )
