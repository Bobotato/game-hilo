from random import seed

from hilo.models.card import Card, Ranks, Suits
from hilo.models.deck import Deck


def test_deck_init_populate_false_shuffle_false():
    deck = Deck(populate=False, shuffle_deck=False)
    assert deck.cards == []


def test_deck_init_populate_true_shuffle_false(ordered_deck):
    deck = Deck(populate=True, shuffle_deck=False)
    assert deck.cards == ordered_deck


def test_deck_init_populate_false_shuffle_true():
    deck = Deck(populate=False, shuffle_deck=True)
    assert deck.cards == []


def test_deck_init_populate_true_shuffle_true(seeded_deck):
    seed(1)
    deck = Deck(populate=True, shuffle_deck=True)
    assert deck.cards == seeded_deck


def test_draw_card_return_last_card():
    deck = Deck(populate=True, shuffle_deck=False)
    assert deck.draw_card() == Card.create(Ranks.K, Suits.S)


def test_is_deck_empty():
    deck = Deck(populate=False, shuffle_deck=False)
    assert deck.cards == []
    assert deck.is_empty()


def test_generate_full_deck(ordered_deck):
    assert Deck.generate_full_deck() == ordered_deck
