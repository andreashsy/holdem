from typing import List
from models.Card import Card

class HandRanker:
    def __init__(self, hand: List[Card]) -> None:
        if len(hand) != 5:
            raise ValueError(f'Hand must contain 5 cards, got {len(hand)}')
        cards_repr = [repr(card) for card in hand]
        if len(set(cards_repr)) != len(hand):
            raise ValueError(f'Cards passed in are not unique, got {cards_repr}')

        self.hand = hand





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