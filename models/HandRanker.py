from collections import Counter
from typing import Callable

from models.Card import Card
from models.Rank import Rank
from models.HandRank import HandRank
from models.HandRankTieBreaker import get_tie_break_values_high_card

class HandRanker:
    def __init__(self, hand: list[Card]) -> None:
        if len(hand) != 5:
            raise ValueError(f'Hand must contain 5 cards, got {len(hand)}')
        cards_repr = [repr(card) for card in hand]
        if len(set(cards_repr)) != len(hand):
            raise ValueError(f'Cards passed in are not unique, got {cards_repr}')

        self.hand: list[Card] = hand
        self.is_hand_flush: bool = False
        self.is_hand_straight: bool = False
        self.rank_histogram: list[int] = []
        self.highest_rank: str = ""
        self.hand_rank: HandRank = None
        self.tie_break_value: float = 0.0

    def get_hand_rank(self) -> HandRank:
        return self.hand_rank

    def update_hand_stats(self) -> None:
        self.is_hand_flush = self._is_flush()
        self.is_hand_straight = self._is_straight()
        self.rank_histogram = self._generate_rank_histogram()
        self.highest_rank = self.find_highest_rank(self.hand)
        self.hand_rank = self.calculate_hand_rank()
        self.tie_break_value = self._calculate_tie_break_value()
 
    def _is_flush(self) -> bool:
        hand_suits = [card.suit for card in self.hand]
        return len(set(hand_suits)) == 1

    def _is_straight(self) -> bool:
        rank_order = ['a'] + [member.value for member in Rank]
        hand_size = len(self.hand)
        valid_straights = [set(rank_order[i: i + hand_size]) for i in range(len(rank_order) - hand_size + 1)]
        ranks = [card.rank for card in self.hand]
        return set(ranks) in valid_straights
    
    def _generate_rank_histogram(self) -> list[int]:
        ranks = [card.rank for card in self.hand]
        return sorted([count for count in Counter(ranks).values()], reverse=True)
    
    @staticmethod
    def find_highest_rank(cards: list[Card]) -> str:
        rank_order = [member.value for member in Rank]
        ranks = [card.rank for card in cards]
        max_idx = 0
        for rank in ranks:
            max_idx = max(max_idx, rank_order.index(rank))
        return rank_order[max_idx]
    
    def _calculate_tie_break_value(self) -> float:
        return TIE_BREAKER_MAP[self.hand_rank](self.hand)

    def calculate_hand_rank(self) -> HandRank:
        if not (self.rank_histogram and self.highest_rank):
            raise Exception('Hand stats not initialised')
        
        if self.is_hand_flush and self.is_hand_straight and self.highest_rank == 'a':
            return HandRank.ROYAL_FLUSH
        elif self.is_hand_flush and self.is_hand_straight:
            return HandRank.STRAIGHT_FLUSH
        elif self.rank_histogram == [4, 1]:
            return HandRank.FOUR_OF_A_KIND
        elif self.rank_histogram == [3, 2]:
            return HandRank.FULL_HOUSE
        elif self.is_hand_flush:
            return HandRank.FLUSH
        elif self.is_hand_straight:
            return HandRank.STRAIGHT
        elif self.rank_histogram == [3, 1, 1]:
            return HandRank.THREE_OF_A_KIND
        elif self.rank_histogram == [2, 2, 1]:
            return HandRank.TWO_PAIRS
        elif self.rank_histogram == [2, 1, 1, 1]:
            return HandRank.PAIR
        else:
            return HandRank.HIGH_CARD

HandRankTieBreakerCalculator = Callable[[list[Card]], float]

TIE_BREAKER_MAP: dict[HandRank, HandRankTieBreakerCalculator] = {
    HandRank.HIGH_CARD: get_tie_break_values_high_card,
}

# TODO: add tie breaker returns decimals 

# Poker hand strengths in order, from best to worst - 
# Royal Flush - Same suit, running rank from A - T
# Straight Flush - Flush + straight
# 4 of a kind - 4 cards of same rank
# Full house - 3 cards of same rank + pair
# Flush - 5 cards of same suit
# Straight - 5 consecutive cards
# 3 of a kind - 3 cards of the same rank
# 2 pairs - 2 of 2 cards of same rank
# Pair - 2 cards of same rank
# High Card - Highest rank card

# Use flags and rank counts, then determine best hand though waterfall logic
# http://nsayer.blogspot.com/2007/07/algorithm-for-evaluating-poker-hands.html