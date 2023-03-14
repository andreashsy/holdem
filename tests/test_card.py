import pytest 
from models.Card import Card

def test_card_raises_error_when_initialized_with_invalid_parameters():
    with pytest.raises(ValueError):
        Card('invalid_value','h')
    with pytest.raises(ValueError):
        Card('2','invalid_value')

def test_equality_returns_true_when_equal():
    assert Card('5', 'h') == Card('5', 'h')
    assert Card('t', 'c') == Card('t', 'c')

def test_equality_returns_false_when_not_equal():
    assert Card('5', 'h') != Card('6', 'h')
    assert Card('5', 'h') != Card('5', 'c')
    assert Card('5', 'h') != Card('t', 'd')
