from models.Card import Card


class HoldemPlayer:
    def __init__(self, stack: int) -> None:
        if stack <= 0: raise ValueError("Player's stack must be positive")
        self.stack: int = stack
        self.hole_cards: list[Card] = []
        self.is_active: bool = False
        self.current_bet: int = 0

    def participate(self) -> None:
        self.is_active = True

    def receive_hole_cards(self, cards: list[Card]) -> None:
        if len(cards) != 2: raise ValueError("Player can only receive two cards")
        self.hole_cards = cards

    def bet(self, bet_amount: int) -> None:
        if bet_amount > self.stack: raise ValueError(f'Cannot bet more than stack {self.stack}')
        if bet_amount <= 0: raise ValueError('Cannot bet 0 or less')
        if not self.is_active == True: raise ValueError('Cannot bet when inactive')
        self.current_bet += bet_amount
        self.stack -= bet_amount

    def fold(self) -> None:
        self.is_active = False
        self.current_bet = 0
    # table - 5 cards, player order, player turn, pot size, blinds, min_raise