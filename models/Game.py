from models.Deck import Deck
from models.Player import HoldemPlayer

class HoldemGameState:
    def __init__(self, players: list[HoldemPlayer]) -> None:
        if len(players) < 2: raise ValueError("Game requires at least 2 players")
    # def __init__(self, players: list[Player], deck: Deck, big_blind: int = 2) -> None:
    #     self.players = players
    #     self.deck = deck
    #     self.pot = 0
    #     self.community_cards = []
    #     self.big_blind = big_blind

"""
when all player have joined, init game
shuffle players into random order
post blinds
deal hole cards
wait for all active bets to be equal
deal flop
wait for all active bets to be equal
deal turn
wait for all active bets to be equal
deal river
wait for all active bets to be equal
showdown: reveal last aggresor and winning hand
pot goes to winner
shift player order by 1
jump to post blinds step
"""