from models.HandRanker import HandRanker
from models.Card import Card
from models.CardGenerator import generate_cards
import pytest

def test_handranker_raises_error_when_not_initialized_with_5_cards():
    card1, card2, card3, card4, card5, card6 = generate_cards(['2h', '3d', '4d', '5d', '6d', '7d'])

    with pytest.raises(ValueError):
        hr_no_cards = HandRanker([])
    with pytest.raises(ValueError):
        hr_4_cards = HandRanker([card1, card2, card3, card4])
    with pytest.raises(ValueError):
        hr_6_cards = HandRanker([card1, card2, card3, card4, card5, card6])

def test_handranker_raises_error_when_initialized_with_duplicate_cards():
    card1, card2, card3, card4 = generate_cards(['2h', '3d', '4d', '5d'])

    with pytest.raises(ValueError):
        hr_2_dup = HandRanker([card1, card1, card2, card3, card4])
    with pytest.raises(ValueError):
        hr_3_dup = HandRanker([card1, card1, card1, card3, card4])
    with pytest.raises(ValueError):
        hr_4_dup = HandRanker([card1, card1, card1, card1, card4])
    with pytest.raises(ValueError):
        hr_5_dup = HandRanker([card1, card1, card1, card1, card1])

def test_handranker_is_flush_returns_true_for_all_suits():
    assert HandRanker(generate_cards(['3d', '4d', '5d', '6d', '7d'])).is_flush() == True
    assert HandRanker(generate_cards(['3h', '4h', '5h', '6h', '7h'])).is_flush() == True
    assert HandRanker(generate_cards(['3s', '4s', '5s', '6s', '7s'])).is_flush() == True
    assert HandRanker(generate_cards(['3c', '4c', '5c', '6c', '7c'])).is_flush() == True

def test_handranker_is_flush_returns_false_if_different_suits():
    assert HandRanker(generate_cards(['3c', '4d', '5d', '6d', '7d'])).is_flush() == False
    assert HandRanker(generate_cards(['3c', '4c', '5d', '6d', '7d'])).is_flush() == False
    assert HandRanker(generate_cards(['3c', '4c', '5c', '6d', '7d'])).is_flush() == False
    assert HandRanker(generate_cards(['3c', '4h', '5s', '6c', '7d'])).is_flush() == False

def test_handranker_is_straight_returns_true_when_all_ranks_consecutive():
    assert HandRanker(generate_cards(['ac', '2h', '3s', '4c', '5d'])).is_straight() == True
    assert HandRanker(generate_cards(['2c', '3h', '4s', '5c', '6d'])).is_straight() == True
    assert HandRanker(generate_cards(['3c', '4h', '5s', '6c', '7d'])).is_straight() == True
    assert HandRanker(generate_cards(['ac', 'jh', 'ks', 'qc', 'td'])).is_straight() == True
    assert HandRanker(generate_cards(['9c', 'jh', 'ks', 'qc', 'td'])).is_straight() == True
    assert HandRanker(generate_cards(['9c', 'jh', '8s', 'qc', 'td'])).is_straight() == True

def test_handranker_is_straight_returns_false_when_ranks_not_consecutive():
    assert HandRanker(generate_cards(['9c', '2h', '8s', 'qc', 'td'])).is_straight() == False
    assert HandRanker(generate_cards(['ac', 'jh', 'ks', 'qc', '2d'])).is_straight() == False
    assert HandRanker(generate_cards(['ac', '3h', 'ks', 'qc', '2d'])).is_straight() == False
    assert HandRanker(generate_cards(['9c', '9h', '8s', 'qc', 'td'])).is_straight() == False