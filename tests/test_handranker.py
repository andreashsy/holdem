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
