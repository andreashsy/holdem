import pytest 
from models.Card import Card
from models.Rank import Rank
from models.Suit import Suit

def test_card_raises_error_when_initialized_with_invalid_parameters():
    with pytest.raises(ValueError):
        Card('invalid_value',Suit('h'))
    with pytest.raises(ValueError):
        Card(Rank('2'),'invalid_value')

def test_card_initialises():
    Card(Rank('a'), Suit('h'))

def test_equality_returns_true_when_equal():
    assert Card(Rank('5'), Suit('h')) == Card(Rank('5'), Suit('h'))
    assert Card(Rank('t'), Suit('c')) == Card(Rank('t'), Suit('c'))

def test_equality_returns_false_when_not_equal():
    assert Card(Rank('5'), Suit('h')) != Card(Rank('6'), Suit('h'))
    assert Card(Rank('5'), Suit('h')) != Card(Rank('5'), Suit('c'))
    assert Card(Rank('5'), Suit('h')) != Card(Rank('t'), Suit('d'))

def test_card_comparison_by_rank():
    assert Card(Rank('2'), Suit('h')) < Card(Rank('3'), Suit('c'))
    assert Card(Rank('3'), Suit('h')) < Card(Rank('4'), Suit('c'))
    assert Card(Rank('4'), Suit('h')) < Card(Rank('5'), Suit('c'))
    assert Card(Rank('5'), Suit('h')) < Card(Rank('6'), Suit('c'))
    assert Card(Rank('6'), Suit('h')) < Card(Rank('7'), Suit('c'))
    assert Card(Rank('7'), Suit('h')) < Card(Rank('8'), Suit('c'))
    assert Card(Rank('8'), Suit('h')) < Card(Rank('9'), Suit('c'))
    assert Card(Rank('9'), Suit('h')) < Card(Rank('t'), Suit('c'))
    assert Card(Rank('t'), Suit('h')) < Card(Rank('j'), Suit('c'))
    assert Card(Rank('j'), Suit('h')) < Card(Rank('q'), Suit('c'))
    assert Card(Rank('q'), Suit('h')) < Card(Rank('k'), Suit('c'))
    assert Card(Rank('k'), Suit('h')) < Card(Rank('a'), Suit('c'))