from random import seed

import pytest

from hilo.models.card import Card
from hilo.models.deck import Deck


@pytest.fixture
def ordered_deck():
    return [
        Card("A", "D"),
        Card("2", "D"),
        Card("3", "D"),
        Card("4", "D"),
        Card("5", "D"),
        Card("6", "D"),
        Card("7", "D"),
        Card("8", "D"),
        Card("9", "D"),
        Card("10", "D"),
        Card("J", "D"),
        Card("Q", "D"),
        Card("K", "D"),
        Card("A", "C"),
        Card("2", "C"),
        Card("3", "C"),
        Card("4", "C"),
        Card("5", "C"),
        Card("6", "C"),
        Card("7", "C"),
        Card("8", "C"),
        Card("9", "C"),
        Card("10", "C"),
        Card("J", "C"),
        Card("Q", "C"),
        Card("K", "C"),
        Card("A", "H"),
        Card("2", "H"),
        Card("3", "H"),
        Card("4", "H"),
        Card("5", "H"),
        Card("6", "H"),
        Card("7", "H"),
        Card("8", "H"),
        Card("9", "H"),
        Card("10", "H"),
        Card("J", "H"),
        Card("Q", "H"),
        Card("K", "H"),
        Card("A", "S"),
        Card("2", "S"),
        Card("3", "S"),
        Card("4", "S"),
        Card("5", "S"),
        Card("6", "S"),
        Card("7", "S"),
        Card("8", "S"),
        Card("9", "S"),
        Card("10", "S"),
        Card("J", "S"),
        Card("Q", "S"),
        Card("K", "S"),
    ]


@pytest.fixture
def seeded_deck():
    return [
        Card("J", "S"),
        Card("10", "D"),
        Card("Q", "H"),
        Card("10", "C"),
        Card("3", "D"),
        Card("K", "H"),
        Card("7", "C"),
        Card("Q", "D"),
        Card("10", "H"),
        Card("6", "D"),
        Card("4", "H"),
        Card("K", "S"),
        Card("5", "S"),
        Card("3", "C"),
        Card("J", "C"),
        Card("8", "S"),
        Card("9", "S"),
        Card("9", "C"),
        Card("2", "S"),
        Card("A", "S"),
        Card("K", "D"),
        Card("Q", "S"),
        Card("7", "H"),
        Card("8", "C"),
        Card("K", "C"),
        Card("A", "H"),
        Card("9", "H"),
        Card("J", "D"),
        Card("8", "H"),
        Card("4", "D"),
        Card("6", "C"),
        Card("2", "C"),
        Card("5", "C"),
        Card("6", "S"),
        Card("A", "D"),
        Card("2", "H"),
        Card("4", "S"),
        Card("2", "D"),
        Card("7", "S"),
        Card("7", "D"),
        Card("A", "C"),
        Card("Q", "C"),
        Card("3", "S"),
        Card("5", "H"),
        Card("3", "H"),
        Card("6", "H"),
        Card("8", "D"),
        Card("4", "C"),
        Card("5", "D"),
        Card("10", "S"),
        Card("J", "H"),
        Card("9", "D"),
    ]


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


def test_cards_getter():
    deck = Deck(populate=False, shuffle_deck=False)
    deck.cards.append(Card("A", "H"))
    assert deck.cards == [Card("A", "H")]


def test_cards_setter():
    deck = Deck(populate=False, shuffle_deck=False)
    deck.cards = [Card("A", "H")]
    assert deck.cards == [Card("A", "H")]


def test_draw_card_return_last_card():
    deck = Deck(populate=True, shuffle_deck=False)
    assert deck.draw_card() == Card("K", "S")


def test_is_deck_empty():
    deck = Deck(populate=False, shuffle_deck=False)
    assert deck.cards == []
    assert deck.is_empty()


def test_generate_full_deck(ordered_deck):
    assert Deck.generate_full_deck() == ordered_deck
