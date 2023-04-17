from models.Card import Card
from models.Rank import Rank
from models.Constants import RANK_VALUE_MAP


def ranks_to_decimals(ranks: list[Rank]) -> float:
    """Converts first rank to first 2 significant decimals, 
    second rank to second 2 significant decimals, etc
    and returns the sum"""
    if not all(isinstance(x, Rank) for x in ranks): raise ValueError('Elements must be of type Rank')
    if len(ranks) > 8: raise ValueError('Cannot have more than 8 elements')

    mapped_rank_values = [RANK_VALUE_MAP[rank] for rank in ranks]
    converted_rank_values = [to_rounded_decimal_position(val, pos) for pos, val in enumerate(mapped_rank_values, 1)]
    return round(sum(converted_rank_values), 16)

def to_rounded_decimal_position(val: int, pos: int) -> float:
    """Converts first position to first 2 significant decimals,
    second position to second 2 decimals, etc.
    Max 8th position due to floating point arithmetic"""
    if not 0 < pos < 9: raise ValueError("Position must be between 1 and 8 inclusive")
    if not 0 < val < 100: raise ValueError("Value must be between 1 and 99 inclusive")

    decimal = val * 10**(pos*-2)
    return round(decimal, 16)

def get_tie_break_values_high_card(hand: list[Card]) -> float:
    hand_ranks_desc = [card.rank for card in sorted(hand, reverse=True)]
    # return hand_desc_sort
    return ranks_to_decimals(hand_ranks_desc)