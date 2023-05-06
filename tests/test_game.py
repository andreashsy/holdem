import pytest
from models.CardGenerator import generate_cards

from models.Game import HoldemGameState
from models.Player import HoldemPlayer
from models.GamePhase import HoldemGamePhase

def test_holdemgamestate_raises_if_initialised_with_less_than_2_players():
    with pytest.raises(ValueError):
        HoldemGameState(players=[])
    with pytest.raises(ValueError):
        HoldemGameState(players=[HoldemPlayer(stack=5)])

def test_holdemgamestate_initialises_at_pregame_phase():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)

    assert game.phase == HoldemGamePhase.PREGAME

def test_holdemgamestate_has_same_players_as_initialised():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)

    assert game.players == players

def test_are_all_players_active_returns_true_if_all_players_active():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)

    assert game.are_all_players_active() == True

def test_are_all_players_active_returns_false_if_one_player_not_active():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)

    assert game.are_all_players_active() == False

def test_are_all_players_active_returns_false_if_all_players_not_active():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    players = [p1, p2]
    game = HoldemGameState(players=players)

    assert game.are_all_players_active() == False

def test_start_preflop_changes_phase_to_preflop_if_phase_in_pregame():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()

    assert game.phase == HoldemGamePhase.PREFLOP

def test_start_preflop_changes_phase_to_preflop_if_phase_in_showdown():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.phase = HoldemGamePhase.SHOWDOWN
    game.start_preflop()

    assert game.phase == HoldemGamePhase.PREFLOP

def test_start_preflop_raises_if_not_all_bets_zero():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    p2.bet(1)
    players = [p1, p2]
    game = HoldemGameState(players=players)
    with pytest.raises(ValueError):
        game.start_preflop()

def test_start_preflop_raises_if_game_not_in_pregame_or_showdown_phase():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)
    
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREFLOP
        game.start_preflop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.FLOP
        game.start_preflop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.TURN
        game.start_preflop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.RIVER
        game.start_preflop()

def test_start_flop_changes_phase_to_flop():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()

    assert game.phase == HoldemGamePhase.FLOP

def test_start_flop_raises_if_game_not_in_preflop():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)
    
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREGAME
        game.start_flop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.FLOP
        game.start_flop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.TURN
        game.start_flop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.RIVER
        game.start_flop()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.SHOWDOWN
        game.start_flop()

def test_start_flop_deals_3_cards_to_community_cards():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()

    assert len(game.get_community_cards()) == 3

def test_start_turn_changes_phase_to_turn():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()
    game.start_turn()

    assert game.phase == HoldemGamePhase.TURN

def test_start_turn_raises_if_game_not_in_flop():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)
    
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREGAME
        game.start_turn()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREFLOP
        game.start_turn()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.TURN
        game.start_turn()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.RIVER
        game.start_turn()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.SHOWDOWN
        game.start_turn()

def test_start_turn_causes_community_cards_to_have_4_cards():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()
    game.start_turn()

    assert len(game.get_community_cards()) == 4

def test_start_river_changes_phase_to_river():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()
    game.start_turn()
    game.start_river()

    assert game.phase == HoldemGamePhase.RIVER

def test_start_river_raises_if_game_not_in_turn():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)
    
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREGAME
        game.start_river()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREFLOP
        game.start_river()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.FLOP
        game.start_river()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.RIVER
        game.start_river()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.SHOWDOWN
        game.start_river()

def test_start_showdown_changes_phase_to_river():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()
    game.start_turn()
    game.start_river()
    game.start_showdown()

    assert game.phase == HoldemGamePhase.SHOWDOWN

def test_start_showdown_raises_if_game_not_in_river():
    players = [HoldemPlayer(stack=5, id="p1"), HoldemPlayer(stack=7, id="p2")]
    game = HoldemGameState(players=players)
    
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREGAME
        game.start_showdown()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.PREFLOP
        game.start_showdown()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.FLOP
        game.start_showdown()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.TURN
        game.start_showdown()
    with pytest.raises(ValueError):
        game.phase = HoldemGamePhase.SHOWDOWN
        game.start_showdown()

def test_start_river_causes_community_cards_to_have_5_cards():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)
    game.start_preflop()
    game.start_flop()
    game.start_turn()
    game.start_river()

    assert len(game.get_community_cards()) == 5

def test_advance_button_position_shifts_2_player_order_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)

    game.advance_button_position()

    assert game.players == [p2, p1]

def test_advance_button_position_shifts_5_player_order_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.advance_button_position()

    assert game.players == [p2, p3, p4, p5, p1]

def test_pay_blinds_deduct_default_blinds_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.pay_blinds()

    p4_bet = p4.get_current_bet()
    p5_bet = p5.get_current_bet()
    assert p5_bet == 2
    assert p4_bet == 1

def test_pay_blinds_deduct_custom_blinds_correctly():
    p1 = HoldemPlayer(stack=50, id="p1")
    p2 = HoldemPlayer(stack=70, id="p2")
    p3 = HoldemPlayer(stack=70, id="p3")
    p4 = HoldemPlayer(stack=70, id="p4")
    p5 = HoldemPlayer(stack=70, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    players = [p1, p2, p3, p4, p5]
    big_blind = 10
    small_blind = 4
    game = HoldemGameState(players=players, big_blind=big_blind, small_blind=small_blind)

    game.pay_blinds()

    p4_bet = p4.get_current_bet()
    p5_bet = p5.get_current_bet()
    assert p5_bet == big_blind
    assert p4_bet == small_blind

def test_deal_hole_cards_gives_2_players_2_cards_each():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p1.participate()
    p2.participate()
    players = [p1, p2]
    game = HoldemGameState(players=players)

    game.prepare_deck()
    game.deal_hole_cards()

    assert len(p1.hole_cards) == 2
    assert len(p2.hole_cards) == 2

def test_deal_hole_cards_gives_5_players_2_cards_each():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.prepare_deck()
    game.deal_hole_cards()

    assert len(p1.hole_cards) == 2
    assert len(p2.hole_cards) == 2
    assert len(p3.hole_cards) == 2
    assert len(p4.hole_cards) == 2
    assert len(p5.hole_cards) == 2

def test_are_all_bets_zero_returns_true_if_all_zero():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    assert game.are_all_bets(0) == True

def test_are_all_bets_zero_returns_false_if_one_not_zero():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p1.bet(1)
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    assert game.are_all_bets(0) == False

def test_are_all_active_bets_one_returns_true_if_all_one_and_all_active():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    p1.bet(1)
    p2.bet(1)
    p3.bet(1)
    p4.bet(1)
    p5.bet(1)
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    assert game.are_all_active_bets(1) == True

def test_are_all_active_bets_one_returns_true_if_all_active_one_and_some_not_active():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    p1.bet(1)
    p2.bet(1)
    p3.bet(1)
    p4.bet(1)
    p5.bet(2)
    p5.fold()
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    assert game.are_all_active_bets(1) == True

def test_are_all_active_bets_one_returns_false_if_one_not_one_and_all_active():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    p1.bet(1)
    p2.bet(1)
    p3.bet(1)
    p4.bet(1)
    p5.bet(2)
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    assert game.are_all_active_bets(1) == False

def test_generate_betting_order_raises_when_pregame_state():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.phase = HoldemGamePhase.PREGAME

    with pytest.raises(ValueError):
        game.generate_betting_order()

def test_generate_betting_order_raises_when_showdown_state():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.phase = HoldemGamePhase.SHOWDOWN

    with pytest.raises(ValueError):
        game.generate_betting_order()

def test_generate_betting_order_generates_preflop_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)
    
    game.phase = HoldemGamePhase.PREFLOP
    player_order = game.generate_betting_order()

    assert player_order == [p1, p2, p3, p4, p5]

def test_generate_betting_order_generates_flop_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)
    
    game.phase = HoldemGamePhase.FLOP
    player_order = game.generate_betting_order()

    assert player_order == [p4, p5, p1, p2, p3]

def test_generate_betting_order_generates_turn_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)
    
    game.phase = HoldemGamePhase.TURN
    player_order = game.generate_betting_order()

    assert player_order == [p4, p5, p1, p2, p3]

def test_generate_betting_order_generates_river_correctly():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)
    
    game.phase = HoldemGamePhase.RIVER
    player_order = game.generate_betting_order()

    assert player_order == [p4, p5, p1, p2, p3]

def test_move_player_bets_to_pot_moves_all_bets_to_pot():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    p1.bet(1)
    p2.bet(2)
    p3.bet(3)
    p4.bet(4)
    p5.bet(6)
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.move_player_bets_to_pot()

    assert game.pot == 1 + 2 + 3 + 4 + 6

def test_move_player_bets_to_pot_changes_all_player_bets_to_zero():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p4 = HoldemPlayer(stack=7, id="p4")
    p5 = HoldemPlayer(stack=7, id="p5")
    p1.participate()
    p2.participate()
    p3.participate()
    p4.participate()
    p5.participate()
    p1.bet(1)
    p2.bet(2)
    p3.bet(3)
    p4.bet(4)
    p5.bet(6)
    players = [p1, p2, p3, p4, p5]
    game = HoldemGameState(players=players)

    game.move_player_bets_to_pot()

    assert p1.get_current_bet() == 0
    assert p2.get_current_bet() == 0
    assert p3.get_current_bet() == 0
    assert p4.get_current_bet() == 0
    assert p5.get_current_bet() == 0

def test_get_active_player_hand_strengths_raises_if_not_showdown():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    players = [p1, p2]
    game = HoldemGameState(players=players)
    
    game.phase = HoldemGamePhase.PREGAME
    with pytest.raises(ValueError):
        game.get_active_player_hand_strengths()

    game.phase = HoldemGamePhase.PREFLOP
    with pytest.raises(ValueError):
        game.get_active_player_hand_strengths()

    game.phase = HoldemGamePhase.FLOP
    with pytest.raises(ValueError):
        game.get_active_player_hand_strengths()

    game.phase = HoldemGamePhase.TURN
    with pytest.raises(ValueError):
        game.get_active_player_hand_strengths()

    game.phase = HoldemGamePhase.RIVER
    with pytest.raises(ValueError):
        game.get_active_player_hand_strengths()

def test_get_active_player_hand_strengths_returns_only_active_player_hand_strengths():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p1.participate()
    p3.participate()
    players = [p1, p2, p3]
    game = HoldemGameState(players=players)    
    
    game.phase = HoldemGamePhase.SHOWDOWN
    p1.hole_cards = generate_cards(['ah', 'as'])
    p2.hole_cards = generate_cards(['7d', '7s'])
    p3.hole_cards = generate_cards(['5h', '6h'])
    game.community_cards = generate_cards(['ad', '2s', '4h', '3s', 'kh'])
    result = game.get_active_player_hand_strengths()

    assert result == [('p1', 4.131203), ('p3', 5.05)]

def test_determine_winner_returns_correct_winner():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p1.participate()
    p3.participate()
    players = [p1, p2, p3]
    game = HoldemGameState(players=players)    
    
    game.phase = HoldemGamePhase.SHOWDOWN
    p1.hole_cards = generate_cards(['ah', 'as'])
    p2.hole_cards = generate_cards(['7d', '7s'])
    p3.hole_cards = generate_cards(['5h', '6h'])
    game.community_cards = generate_cards(['ad', '2s', '4h', '3s', 'kh'])
    winner = game.determine_winners()

    assert winner == [p3]

def test_determine_winner_returns_correct_winners_if_draw():
    p1 = HoldemPlayer(stack=5, id="p1")
    p2 = HoldemPlayer(stack=7, id="p2")
    p3 = HoldemPlayer(stack=7, id="p3")
    p1.participate()
    p2.participate()
    p3.participate()
    players = [p1, p2, p3]
    game = HoldemGameState(players=players)    
    
    game.phase = HoldemGamePhase.SHOWDOWN
    p1.hole_cards = generate_cards(['ah', 'as'])
    p2.hole_cards = generate_cards(['5d', '6s'])
    p3.hole_cards = generate_cards(['5h', '6h'])
    game.community_cards = generate_cards(['ad', '2s', '4h', '3s', 'kh'])
    winner = game.determine_winners()

    assert set(winner) == set([p2, p3])