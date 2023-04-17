import pytest
from models.CardGenerator import generate_cards

from models.Rank import Rank
from models.HandRankTieBreaker import get_tie_break_values_high_card, ranks_to_decimals, to_rounded_decimal_position

def test_ranks_to_decimals_raises_value_error_if_not_ranks():
    with pytest.raises(ValueError):
        ranks_to_decimals(['a', 'k'])

def test_ranks_to_decimals_raises_value_error_if_more_than_8_ranks():
    with pytest.raises(ValueError):
        ranks_to_decimals([Rank.TWO] * 9)

def test_ranks_to_decimals_returns_RankTWO_correctly():
    assert ranks_to_decimals([Rank.TWO]) == 0.01

def test_ranks_to_decimals_returns_RankSEVEN_correctly():
    assert ranks_to_decimals([Rank.SEVEN]) == 0.06

def test_ranks_to_decimals_returns_RankACE_correctly():
    assert ranks_to_decimals([Rank.ACE]) == 0.13

def test_ranks_to_decimals_returns_8_ranks_correctly():
    assert ranks_to_decimals([Rank.ACE, Rank.TWO, Rank.FOUR, Rank.JACK, Rank.SIX, Rank.KING, Rank.QUEEN, Rank.TEN]) == 0.1301031005121109

def test_ranks_to_decimals_returns_5_ranks_correctly():
    assert ranks_to_decimals([Rank.THREE, Rank.FIVE, Rank.EIGHT, Rank.FOUR, Rank.NINE]) == 0.0204070308

def test_to_rounded_decimal_position_raises_value_error_if_position_more_than_8():
    with pytest.raises(ValueError):
        to_rounded_decimal_position(1, 9)

def test_to_rounded_decimal_position_raises_value_error_if_position_less_than_1():
    with pytest.raises(ValueError):
        to_rounded_decimal_position(1, 0)

def test_to_rounded_decimal_position_raises_value_error_if_value_more_than_99():
    with pytest.raises(ValueError):
        to_rounded_decimal_position(100, 1)

def test_to_rounded_decimal_position_raises_value_error_if_value_less_than_1():
    with pytest.raises(ValueError):
        to_rounded_decimal_position(0, 1)

def test_to_rounded_decimal_position_correct_when_value_is_1():
    assert to_rounded_decimal_position(1, 2) == 0.0001

def test_to_rounded_decimal_position_correct_when_value_is_99():
    assert to_rounded_decimal_position(99, 2) == 0.0099

def test_to_rounded_decimal_position_correct_when_position_is_1():
    assert to_rounded_decimal_position(5, 1) == 0.05

def test_to_rounded_decimal_position_correct_when_position_is_8():
    assert to_rounded_decimal_position(5, 8) == 0.0000000000000005

def test_get_tie_break_values_high_card_returns_correct_value():
    hand = generate_cards(['9c', '2h', '8s', 'qc', 'td'])

    assert get_tie_break_values_high_card(hand) == 0.1109080701