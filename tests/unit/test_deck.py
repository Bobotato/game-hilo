from random import seed

import pytest

from hilo.models.card import Card
from hilo.models.deck import Deck


def test_deck_init_populate_false_shuffle_false():
    test_deck = Deck(populate=False, shuffle_deck=False)
    assert test_deck.cards == []


def test_deck_init_populate_true_shuffle_false(ordered_deck):
    test_deck = Deck(populate=True, shuffle_deck=False)
    assert test_deck.cards == ordered_deck


def test_deck_init_populate_false_shuffle_true():
    test_deck = Deck(populate=False, shuffle_deck=True)
    assert test_deck.cards == []


def test_deck_init_populate_true_shuffle_true(seeded_deck):
    seed(1)
    dummy_deck = Deck(populate=True, shuffle_deck=True)
    assert dummy_deck.cards == seeded_deck


def test_cards_getter():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    dummy_deck.cards.append(Card("A", "H"))
    assert dummy_deck.cards == [Card("A", "H")]


def test_cards_setter():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    dummy_deck.cards = [Card("A", "H")]
    assert dummy_deck.cards == [Card("A", "H")]


def test_cards_setter_invalid_card():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    with pytest.raises(ValueError):
        dummy_deck.cards = ["test"]


def test_draw_card_return_last_card():
    dummy_deck = Deck(populate=True, shuffle_deck=False)
    assert dummy_deck.draw_card() == Card("K", "S")


def test_is_deck_empty():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    assert dummy_deck.cards == []
    assert dummy_deck.is_empty()


def test_generate_full_deck(ordered_deck):
    assert Deck.generate_full_deck() == ordered_deck


def test_deck_repr():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    dummy_deck.cards = [Card("K", "S")]
    assert repr(dummy_deck) == "[KS]"
