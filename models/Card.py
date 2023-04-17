from models.Rank import Rank
from models.Suit import Suit
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Card:
    rank: Rank
    suit: Suit

    def __post_init__(self) -> None:
        if not isinstance(self.rank, Rank):
            raise ValueError(f'Rank should be of type Rank, got {type(self.rank)}')
        if not isinstance(self.suit, Suit):
            raise ValueError(f'Suit should be of type Suit, got {type(self.suit)}')

    def __str__(self) -> str:
        return f'{self.rank.name} OF {self.suit.name}S'

    def __repr__(self) -> str:
        return f'{self.rank.value}{self.suit.value}'