from models.Rank import Rank
from models.Suit import Suit
from models.Constants import CARD_RANKS, CARD_SUITS

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        if rank not in CARD_RANKS:
            raise ValueError(f'Rank invalid, got {rank}')
        if suit not in CARD_SUITS:
            raise ValueError(f'Suit invalid, got {suit}')
        self.rank = rank
        self.suit = suit


    def __str__(self) -> str:
        return f'{Rank(self.rank).name} OF {Suit(self.suit).name}S'

    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}'