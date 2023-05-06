import pytest
from models.Card import Card
from models.CardGenerator import generate_cards
from models.Rank import Rank
from models.Suit import Suit

def test_generate_cards_empty_list_returns_empty_list():
    assert generate_cards([]) == []   

def test_generate_cards_generates_one_card():
    assert generate_cards(['5h']) == [Card(Rank('5'), Suit('h'))]
    assert generate_cards(['as']) == [Card(Rank('a'), Suit('s'))]
    assert generate_cards(['tc']) == [Card(Rank('t'), Suit('c'))]
    assert generate_cards(['kd']) == [Card(Rank('k'), Suit('d'))]

def test_generate_cards_generates_cards_in_order():
    assert generate_cards(['kd', 'qc', 'ts', '4h']) == [Card(Rank('k'), Suit('d')), Card(Rank('q'), Suit('c')), Card(Rank('t'), Suit('s')), Card(Rank('4'), Suit('h'))]
    
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
