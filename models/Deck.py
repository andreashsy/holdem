import random
from Card import Card
from Constants import CARD_SUITS, CARD_RANKS

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(r, s) for r in CARD_RANKS for s in CARD_SUITS]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise AttributeError('No more cards in deck')
        return self.cards.pop()