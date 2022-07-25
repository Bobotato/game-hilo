from hilo.models.card import Card, Ranks, Suits
from hilo.models.roundresult import RoundResult


def test_round_result_init():
    roundresult = RoundResult(
        drawn_card=Card.create(Ranks.A, Suits.H),
        win=True,
        is_player_bankrupt=True,
        is_deck_empty=True,
    )
    assert roundresult.drawn_card == Card.create(Ranks.A, Suits.H)
    assert roundresult.win
    assert roundresult.is_player_bankrupt
    assert roundresult.is_deck_empty
