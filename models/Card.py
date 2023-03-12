from models.Rank import Rank
from models.Suit import Suit
from models.Constants import CARD_RANKS, CARD_SUITS
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Card:
    rank: str
    suit: str

    def __post_init__(self) -> None:
        if self.rank not in CARD_RANKS:
            raise ValueError(f'Rank invalid, got {self.rank}')
        if self.suit not in CARD_SUITS:
            raise ValueError(f'Suit invalid, got {self.suit}')

    def __str__(self) -> str:
        return f'{Rank(self.rank).name} OF {Suit(self.suit).name}S'

    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}'