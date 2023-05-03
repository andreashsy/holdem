from models.Card import Card
from models.Deck import Deck
from models.Player import HoldemPlayer
from models.GamePhase import HoldemGamePhase
import random

class HoldemGameState:
    def __init__(self, players: list[HoldemPlayer], big_blind: int=2, small_blind: int=1) -> None:
        if len(players) < 2: raise ValueError("Game requires at least 2 players")
        self.players = players
        self.phase = HoldemGamePhase.PREGAME
        self.deck = None
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.community_cards = []
        # self.active_player_index = None

    def start_preflop(self) -> None:
        if not self.are_all_bets(0): raise ValueError('All bets must be zero')
        if self.phase == HoldemGamePhase.PREGAME:
            self.shuffle_players()
        elif self.phase == HoldemGamePhase.SHOWDOWN:
            self.advance_button()
        else: 
            raise ValueError(f"Game phase must be pregame or showdown. Current mode is {self.phase}")
        self.phase = HoldemGamePhase.PREFLOP
        self.prepare_deck()
        self.pay_blinds()
        self.deal_hole_cards()
    
    def start_flop(self) -> None:
        if not self.phase == HoldemGamePhase.PREFLOP: raise ValueError(f"Game must be in preflop. Current mode is {self.phase}")
        self.phase = HoldemGamePhase.FLOP
        card1, card2, card3 = self.deck.draw_card(), self.deck.draw_card(), self.deck.draw_card()
        self.community_cards.extend([card1, card2, card3])

    def start_turn(self) -> None:
        if not self.phase == HoldemGamePhase.FLOP: raise ValueError(f"Game must be in flop. Current mode is {self.phase}")
        self.phase = HoldemGamePhase.TURN
        self.community_cards.append(self.deck.draw_card())

    def start_river(self) -> None:
        if not self.phase == HoldemGamePhase.TURN: raise ValueError(f"Game must be in turn. Current mode is {self.phase}")
        self.phase = HoldemGamePhase.RIVER
        self.community_cards.append(self.deck.draw_card())

    def start_showdown(self) -> None:
        if not self.phase == HoldemGamePhase.RIVER: raise ValueError(f"Game must be in river. Current mode is {self.phase}")
        self.phase = HoldemGamePhase.SHOWDOWN

    def initiate_betting_round(self) -> None:
        pass


    def advance_button(self) -> None:
        self.players = self.players[1:] + [self.players[0]]

    def prepare_deck(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

    def shuffle_players(self) -> None:
        random.shuffle(self.players)

    def pay_blinds(self) -> None:
        self.players[-1].bet(self.big_blind)
        self.players[-2].bet(self.small_blind)

    def deal_hole_cards(self) -> None:
        for player in self.players:
            card1, card2 = self.deck.draw_card(), self.deck.draw_card()
            player.hole_cards.extend([card1, card2])

    def are_all_players_active(self) -> bool:
        return all([player.is_active for player in self.players])
    
    def are_all_bets(self, bet_value: int) -> bool:
        return all([player.get_current_bet() == bet_value for player in self.players])
    
    def are_all_active_bets(self, bet_value: int) -> bool:
        return all([player.get_current_bet() == bet_value for player in self.players if player.is_active])

    def get_community_cards(self) -> list[Card]:
        return self.community_cards
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