import pytest
from card import Card


def test_card_ok():
    ten_red = Card(10, "red")
    assert ten_red.value == 10
    assert ten_red.color == "red"


def test_card_invalid_value():
    with pytest.raises(AttributeError):
        Card(0, "red")

    with pytest.raises(AttributeError):
        Card(15, "red")

    with pytest.raises(AttributeError):
        Card("abcdef", "red")


def test_card_value_string():
    ten_red = Card("10", "red")
    assert ten_red.value == 10
    assert ten_red.color == "red"


def test_card_invalid_color():
    with pytest.raises(AttributeError):
        Card(10, "blue")


def test_stronger_than():
    five_black = Card(5, "black")
    ten_red = Card(10, "red")
    one_red = Card(1, "red")

    assert ten_red.is_stronger_than(five_black)
    assert one_red.is_stronger_than(ten_red) is False
