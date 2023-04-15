from collections import Counter
from models.Card import Card
from models.Rank import Rank
from models.HandRank import HandRank

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

    def update_hand_stats(self) -> None:
        self.is_hand_flush = self._is_flush()
        self.is_hand_straight = self._is_straight()
        self.rank_histogram = self._generate_rank_histogram()
        self.highest_rank = self.get_highest_rank(self.hand)
        self.hand_rank = self.calculate_hand_rank()
 
    def _is_flush(self) -> bool:
        hand_suits = [card.suit for card in self.hand]
        return len(set(hand_suits)) == 1

    def _is_straight(self) -> bool:
        rank_order = ['a'] + [member.value for member in Rank]
        HAND_SIZE = 5
        valid_straights = [set(rank_order[i: i + HAND_SIZE]) for i in range(len(rank_order) - HAND_SIZE + 1)]
        ranks = [card.rank for card in self.hand]
        return set(ranks) in valid_straights
    
    def _generate_rank_histogram(self) -> list[int]:
        ranks = [card.rank for card in self.hand]
        return sorted([count for count in Counter(ranks).values()], reverse=True)
    
    @staticmethod
    def get_highest_rank(cards: list[Card]) -> str:
        rank_order = [member.value for member in Rank]
        ranks = [card.rank for card in cards]
        max_idx = 0
        for rank in ranks:
            max_idx = max(max_idx, rank_order.index(rank))
        return rank_order[max_idx]

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

# TODO: add tie breaker class which returns  decimals 

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