from models.HandRanker import HandRanker
from models.Card import Card
import pytest

def test_handranker_raises_error_when_not_initialized_with_5_cards():
    card1, card2, card3, card4, card5, card6 = Card('2', 'h'), Card('3', 'd'), Card('4', 'd'), Card('5', 'd'), Card('6', 'd'), Card('7', 'd')

    with pytest.raises(ValueError):
        hr_no_cards = HandRanker([])
    with pytest.raises(ValueError):
        hr_4_cards = HandRanker([card1, card2, card3, card4])
    with pytest.raises(ValueError):
        hr_6_cards = HandRanker([card1, card2, card3, card4, card5, card6])

def test_handranker_raises_error_when_initialized_with_duplicate_cards():
    card1, card2, card3, card4, card5 = Card('3', 'd'), Card('4', 'd'), Card('5', 'd'), Card('6', 'd'), Card('7', 'd')

    with pytest.raises(ValueError):
        hr_2_dup = HandRanker([card1, card1, card2, card3, card4])
    with pytest.raises(ValueError):
        hr_3_dup = HandRanker([card1, card1, card1, card3, card4])
    with pytest.raises(ValueError):
        hr_4_dup = HandRanker([card1, card1, card1, card1, card4])
    with pytest.raises(ValueError):
        hr_5_dup = HandRanker([card1, card1, card1, card1, card1])