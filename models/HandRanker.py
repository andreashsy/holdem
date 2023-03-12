from collections import Counter
from models.Card import Card
from models.Rank import Rank

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
 
    def is_flush(self) -> bool:
        hand_suits = [card.suit for card in self.hand]
        return len(set(hand_suits)) == 1

    def is_straight(self) -> bool:
        rank_order = ['a'] + [member.value for member in Rank]
        HAND_SIZE = 5
        valid_straights = [set(rank_order[i: i + HAND_SIZE]) for i in range(len(rank_order) - HAND_SIZE + 1)]
        ranks = [card.rank for card in self.hand]
        return set(ranks) in valid_straights
    
    def generate_rank_histogram(self) -> list[int]:
        ranks = [card.rank for card in self.hand]
        return [count for count in Counter(ranks).values()]

# Poker hand strengths in order, from best to worst - 
# Royal Flush - Same suit, running numbers from A - T
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