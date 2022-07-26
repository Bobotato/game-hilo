import pytest

from hilo.models.card import Card, Ranks, Suits


# DummyClass for testing eq against non-card object
class DummyClass:
    def __init__(self):
        return

    def __eq__(self, other):
        raise TypeError


def test_card_create():
    card = Card.create(Ranks.A, Suits.D)
    assert card.sort_index == 0
    assert card.rank == Ranks.A
    assert card.suit == Suits.D


def test_card_calculate_sort_index():
    card = Card.create(Ranks.A, Suits.D)
    assert card._Card__calculate_sort_index(Ranks.A, Suits.D) == 0


def test_card_eq():
    assert Card.create(Ranks.A, Suits.D) == Card.create(Ranks.A, Suits.D)


def test_card_eq_not_implemented():
    with pytest.raises(TypeError):
        Card.create(Ranks.A, Suits.D) == DummyClass()


def test_card_gt():
    assert Card.create(Ranks.TWO, Suits.D) > Card.create(Ranks.A, Suits.D)


def test_card_gt_not_implemented():
    with pytest.raises(TypeError):
        Card.create(Ranks.A, Suits.D) > "test"


def test_card_lt():
    assert Card.create(Ranks.A, Suits.D) < Card.create(Ranks.TWO, Suits.D)


def test_card_lt_not_implemented():
    with pytest.raises(TypeError):
        Card.create(Ranks.A, Suits.D) < "test"


def test_card_str():
    card = Card.create(Ranks.A, Suits.D)
    assert str(card) == "A of D"
