from models.BettingRound import BettingRound
from models.Player import HoldemPlayer


def test_get_active_player_returns_first_player_on_initialisation():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player1.participate()
    player2.participate()

    round = BettingRound([player1, player2])

    active_player = round.get_active_player()

    assert active_player == player1

def test_move_to_next_active_player_moves_to_next_player_if_both_active():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player1.participate()
    player2.participate()
    round = BettingRound([player1, player2])

    round.move_to_next_active_player()
    active_player = round.get_active_player()

    assert active_player == player2

def test_move_to_next_active_player_moves_to_next_active_player_if_active_player_is_end_of_list():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player1.participate()
    player2.participate()
    round = BettingRound([player1, player2])

    round.active_player_index = len(round.players) - 1
    round.move_to_next_active_player()
    active_player = round.get_active_player()

    assert active_player == player1


def test_move_to_next_active_player_skips_one_inactive_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.move_to_next_active_player()
    active_player = round.get_active_player()

    assert active_player == player3

def test_get_active_player_skips_inactive_first_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    active_player = round.get_active_player()

    assert active_player == player2

def test_count_active_players_correct_if_all_active():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    num_active_players = round.count_active_players()

    assert num_active_players == 3

def test_count_active_players_correct_if_one_inactive():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    num_active_players = round.count_active_players()

    assert num_active_players == 2

def test_count_active_players_correct_if_none_inactive():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    round = BettingRound([player1, player2, player3])

    num_active_players = round.count_active_players()

    assert num_active_players == 0

def test_are_all_active_players_bet_returns_true_if_all_players_active_and_same_postive_bet():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    player1.bet(6)
    player2.bet(6)
    player3.bet(6)
    round = BettingRound([player1, player2, player3])

    all_active_players_bet_same = round.are_all_active_players_bet(6)

    assert all_active_players_bet_same == True

def test_are_all_active_players_bet_returns_true_if_all_players_active_and_zero_bet():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    all_active_players_bet_same = round.are_all_active_players_bet(0)

    assert all_active_players_bet_same == True

def test_are_all_active_players_bet_returns_true_if_some_players_active_and_positive_active_bets():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player3.participate()
    player1.bet(8)
    player3.bet(8)
    round = BettingRound([player1, player2, player3])

    all_active_players_bet_same = round.are_all_active_players_bet(8)

    assert all_active_players_bet_same == True

def test_bet_action_returns_true_if_player_is_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    is_bet_success = round.bet_action('p1', 4)

    assert is_bet_success == True

def test_bet_action_actually_bets_if_player_is_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 4)

    assert player1.get_current_bet() == 4

def test_bet_action_goes_to_next_active_player_if_player_is_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 4)

    assert round.get_active_player() == player2

def test_bet_action_increases_action_count_if_player_is_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 4)

    assert round.number_of_actions == 1

def test_bet_action_returns_false_if_player_is_not_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    is_bet_success = round.bet_action('p2', 4)

    assert is_bet_success == False

def test_bet_action_returns_false_if_player_is_current_active_player_and_bet_is_not_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    is_bet_success = round.bet_action('p1', 400)

    assert is_bet_success == False

def test_bet_action_does_not_bet_if_player_is_not_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p2', 4)

    assert player1.get_current_bet() == 0
    assert player2.get_current_bet() == 0

def test_bet_action_does_not_bet_if_player_is_current_active_player_and_bet_is_not_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 400)

    assert player1.get_current_bet() == 0

def test_bet_action_does_not_change_active_player_if_player_is_not_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p2', 4)

    assert round.get_active_player() == player1

def test_bet_action_does_not_change_active_player_if_player_is_current_active_player_and_bet_is_not_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 400)

    assert round.get_active_player() == player1

def test_bet_action_does_not_increase_action_count_if_player_is_not_current_active_player_and_bet_is_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p2', 4)

    assert round.number_of_actions == 0

def test_bet_action_does_not_increase_action_count_if_player_is_current_active_player_and_bet_is_not_valid():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 400)

    assert round.number_of_actions == 0

def test_fold_action_returns_true_if_player_is_current_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    is_action_success = round.fold_action('p1')

    assert is_action_success == True

def test_fold_action_returns_false_if_player_is_not_current_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    is_action_success = round.fold_action('p2')

    assert is_action_success == False

def test_fold_action_deactivates_player_if_player_is_current_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p1')

    assert player1.is_active == False

def test_fold_action_does_not_deactive_player_if_player_is_not_current_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p2')

    assert player1.is_active == True
    assert player2.is_active == True

def test_fold_action_increases_number_of_actions_if_player_is_current_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p1')

    assert round.number_of_actions == 1

def test_fold_action_does_not_increase_number_of_actions_if_player_is_not_current_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p2')

    assert round.number_of_actions == 0

def test_is_round_over_returns_true_if_one_active_player():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p1')
    round.fold_action('p2')

    assert round.is_round_over() == True

def test_is_round_over_returns_false_if_two_active_players_with_different_bets():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p1')
    round.bet_action('p2', 1)

    assert round.is_round_over() == False

def test_is_round_over_returns_true_if_all_active_players_same_positive_bet():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.bet_action('p1', 1)
    round.bet_action('p2', 1)
    round.bet_action('p3', 1)

    assert round.is_round_over() == True

def test_is_round_over_returns_true_if_active_players_same_positive_bet():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    round.fold_action('p1')
    round.bet_action('p2', 1)
    round.bet_action('p3', 1)

    assert round.is_round_over() == True

def test_is_round_over_returns_false_not_all_players_moved():
    player1 = HoldemPlayer(20, "p1")
    player2 = HoldemPlayer(20, "p2")
    player3 = HoldemPlayer(20, "p3")
    player1.participate()
    player2.participate()
    player3.participate()
    round = BettingRound([player1, player2, player3])

    assert round.is_round_over() == False