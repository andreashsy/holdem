import random
from models.Card import Card
from models.Constants import CARD_SUITS, CARD_RANKS

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(r, s) for r in CARD_RANKS for s in CARD_SUITS]

    def get_cards(self) -> list[Card]:
        return self.cards.copy()

    def size(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise AttributeError('No more cards in deck')
        return self.cards.pop()