import pytest
from models.CardGenerator import generate_cards

from models.Rank import Rank
from models.HandRankTieBreaker import (
    ranks_to_decimals,
    to_rounded_decimal_position,
    get_tie_break_values_high_card,
    get_tie_break_values_pair,
    get_tie_break_values_2_pair,
    get_tie_break_values_3_of_a_kind,
    get_tie_break_values_straight,
    get_tie_break_values_flush,
    get_tie_break_values_full_house,
    get_tie_break_values_4_of_a_kind,
    get_tie_break_values_straight_flush,
    get_tie_break_values_royal_flush
)

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

def test_get_tie_break_values_pair_returns_correct_value():
    hand = generate_cards(['9c', '2h', '2s', 'qc', 'td'])

    assert get_tie_break_values_pair(hand) == 0.01110908

def test_get_tie_break_values_2_pair_returns_correct_value():
    hand = generate_cards(['9c', '2h', '2s', 'qc', '9d'])

    assert get_tie_break_values_2_pair(hand) == 0.080111

def test_get_tie_break_values_3_of_a_kind_returns_correct_value():
    hand = generate_cards(['9c', '2h', '9s', 'qc', '9d'])

    assert get_tie_break_values_3_of_a_kind(hand) == 0.081101

def test_get_tie_break_values_straight_returns_correct_value():
    hand = generate_cards(['9c', 'th', 'js', '8c', '7d'])

    assert get_tie_break_values_straight(hand) == 0.1

def test_get_tie_break_values_straight_returns_correct_value_a2345():
    hand = generate_cards(['ac', '2h', '3s', '5c', '4d'])

    assert get_tie_break_values_straight(hand) == 0.04

def test_get_tie_break_values_flush_returns_correct_value():
    hand = generate_cards(['ac', '2c', '9c', 'qc', '7c'])

    assert get_tie_break_values_flush(hand) == 0.1311080601

def test_get_tie_break_values_full_house_returns_correct_value():
    hand = generate_cards(['kc', 'ks', '9c', '9h', '9d'])

    assert get_tie_break_values_full_house(hand) == 0.0812

def test_get_tie_break_values_4_of_a_kind_returns_correct_value():
    hand = generate_cards(['4c', '4s', 'qc', '4h', '4d'])

    assert get_tie_break_values_4_of_a_kind(hand) == 0.0311

def test_get_tie_break_values_straight_flush_returns_correct_value():
    hand = generate_cards(['9c', 'tc', 'jc', '8c', 'qc'])

    assert get_tie_break_values_straight_flush(hand) == 0.11

def test_get_tie_break_values_straight_flush_returns_correct_value_a2345():
    hand = generate_cards(['ac', '2c', '3c', '5c', '4c'])

    assert get_tie_break_values_straight_flush(hand) == 0.04

def test_get_tie_break_values_royal_flush_returns_correct_value():
    hand = generate_cards(['ac', 'tc', 'jc', 'kc', 'qc'])

    assert get_tie_break_values_royal_flush(hand) == 0.0