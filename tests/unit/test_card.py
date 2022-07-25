from hilo.models.card import Card, Ranks, Suits


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


def test_card_str():
    card = Card.create(Ranks.A, Suits.D)
    assert str(card) == "A of D"
