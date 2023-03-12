from models.CardGenerator import generate_cards
from models.Card import Card
import pytest

def test_generate_cards_empty_list_returns_empty_list():
    assert generate_cards([]) == []   

def test_generate_cards_generates_one_card():
    assert generate_cards(['5h']) == [Card('5', 'h')]
    assert generate_cards(['as']) == [Card('a', 's')]
    assert generate_cards(['tc']) == [Card('t', 'c')]
    assert generate_cards(['kd']) == [Card('k', 'd')]

def test_generate_cards_generates_cards_in_order():
    assert generate_cards(['kd', 'qc', 'ts', '4h']) == [Card('k', 'd'), Card('q', 'c'), Card('t', 's'), Card('4', 'h')]
    
def test_generate_cards_throws_error_when_elements_not_length_two():
    with pytest.raises(ValueError):
        generate_cards(['ttk'])
    with pytest.raises(ValueError):
        generate_cards(['1234'])

def test_generate_cards_throws_error_when_elements_incorrect_type():
    with pytest.raises(TypeError):
        generate_cards([None])
    with pytest.raises(TypeError):
        generate_cards([{'1':'2'}])
