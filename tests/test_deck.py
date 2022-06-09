from random import seed

from hilo.models.card import Card
from hilo.models.deck import Deck

seeded_deck = Deck(populate=False, shuffle_deck=False)
seeded_deck.cards = [
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


def test_deck_init_populate():
    test_deck = Deck(populate=True)
    assert test_deck.cards != []


def test_deck_init_shuffle():
    seed(1)
    dummy_deck = Deck(populate=True, shuffle_deck=True)
    assert dummy_deck.cards == seeded_deck.cards


def test_cards_getter():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    dummy_deck.cards.append(Card("A", "H"))
    assert dummy_deck.cards == [Card("A", "H")]


def test_cards_setter():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    dummy_deck.cards = [Card("A", "H")]
    assert dummy_deck.cards == [Card("A", "H")]


def test_draw_card_return_last_card():
    dummy_deck = Deck(populate=True, shuffle_deck=False)
    assert dummy_deck.draw_card() == Card("K", "S")


def test_is_empty():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    assert dummy_deck.is_empty()


def test_populate():
    dummy_deck = Deck(populate=False, shuffle_deck=False)
    dummy_deck.populate()
    populated_deck = Deck(populate=True, shuffle_deck=False)
    assert dummy_deck.cards == populated_deck.cards
