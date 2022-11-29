class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f'{self.rank}{self.suit}'

    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}'