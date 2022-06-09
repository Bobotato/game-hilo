import pytest

from hilo.models.card import Card


# TestClass is to test if the RHS implementation of __eq__/__ne__
# is used when a Card is compared against a non-Card.
class TestClass:
    def __init__(self):
        return

    def __eq__(self, other):
        raise ZeroDivisionError


def test_suit_getter():
    card = Card("A", "H")
    assert card.suit == "H"


def test_suit_setter():
    card = Card("A", "H")
    card.suit = "S"
    assert card.suit == "S"


def test_suit_setter_invalid_value_raise_ValueError():
    with pytest.raises(ValueError):
        Card("A", "X")


def test_value_getter():
    card = Card("A", "H")
    assert card.value == "A"


def test_value_setter():
    card = Card("A", "H")
    card.value = "10"
    assert card.value == "10"


def test_value_setter_invalid_value_raise_ValueError():
    with pytest.raises(ValueError):
        Card("12", "H")


def test_eq():
    assert Card("A", "H") == Card("A", "H")


def test_eq_handled_by_rhs_when_not_card():
    with pytest.raises(ZeroDivisionError):
        Card("A", "H") == TestClass()


def test_gt_with_alphabetic_value():
    assert Card("K", "H") > Card("A", "H")


def test_gt_with_numerical_value():
    assert Card("10", "S") > Card("2", "S")


def test_gt_with_different_suit():
    assert Card("10", "S") > Card("10", "D")


def test_gt_with_different_value():
    assert Card("5", "H") > Card("4", "H")


def test_gt_not_implemented_raise_TypeError():
    with pytest.raises(TypeError):
        Card("K", "H") > ("Q", "S")


def test_lt_with_alphabetic_value():
    assert Card("A", "H") < Card("K", "H")


def test_lt_with_numerical_value():
    assert Card("2", "H") < Card("10", "H")


def test_lt_with_different_suit():
    assert Card("5", "H") < Card("5", "S")


def test_lt_with_different_value():
    assert Card("5", "H") < Card("10", "H")


def test_lt_not_implemented_raise_TypeError():
    with pytest.raises(TypeError):
        Card("4", "H") < ("10", "H")


def test_ne_with_different_value():
    assert Card("A", "H") != Card("5", "H")


def test_ne_with_different_suit():
    assert Card("A", "H") != Card("A", "S")


def test_ne_handled_by_rhs_when_not_card():
    with pytest.raises(ZeroDivisionError):
        Card("K", "H") != TestClass()
