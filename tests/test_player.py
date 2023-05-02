import pytest

from models.CardGenerator import generate_cards
from models.Player import HoldemPlayer

def test_holdemplayer_raises_if_stack_equals_zero():
    with pytest.raises(ValueError):
        HoldemPlayer(stack=0)

def test_holdemplayer_initialises_as_not_active():
    player = HoldemPlayer(stack=1)

    assert player.is_active == False

def test_holdemplayer_initialises_current_bet_as_zero():
    player = HoldemPlayer(stack=1)

    assert player.current_bet == 0

def test_holdemplayer_can_receive_two_hole_cards():
    player = HoldemPlayer(stack=1)

    cards = generate_cards(["5h", "2c"])

    player.receive_hole_cards(cards)

def test_holdemplayer_raises_if_does_not_receive_exactly_two_cards():
    player = HoldemPlayer(stack=1)

    one_card = generate_cards(['ah'])
    three_cards = generate_cards(['ah', '2c', '4d'])
    five_cards = generate_cards(['7d', '5h', 'kc', 'qd', 'ah'])

    with pytest.raises(ValueError):
        player.receive_hole_cards(one_card)
    with pytest.raises(ValueError):
        player.receive_hole_cards(three_cards)
    with pytest.raises(ValueError):
        player.receive_hole_cards(five_cards)

def test_holdemplayer_two_hole_cards_are_the_same():
    player = HoldemPlayer(stack=1)

    cards = generate_cards(["5h", "2c"])
    player.receive_hole_cards(cards)

    assert player.hole_cards == generate_cards(["5h", "2c"])

def test_holdemplayer_turns_active_when_participating():
    player = HoldemPlayer(stack=1)
    player.participate()

    assert player.is_active == True

def test_holdemplayer_betting_reduces_stack_by_the_bet_amount():
    player = HoldemPlayer(stack=100)
    player.participate()

    player.bet(27)

    assert player.stack == 100-27

    player.bet(5)

    assert player.stack == 100-27-5

def test_holdemplayer_betting_increases_current_bet_by_the_bet_amount():
    player = HoldemPlayer(stack=100)
    player.participate()

    player.bet(27)

    assert player.current_bet == 27

    player.bet(15)

    assert player.current_bet == 27 + 15

def test_holdemplayer_raises_if_bets_more_than_current_stack():
    player = HoldemPlayer(stack=100)
    player.participate()
    with pytest.raises(ValueError):
        player.bet(101)

def test_holdemplayer_raises_if_bets_lower_than_1():
    player = HoldemPlayer(stack=100)
    player.participate()
    with pytest.raises(ValueError):
        player.bet(0)
    with pytest.raises(ValueError):
        player.bet(-1)

def test_holdem_player_raises_if_betting_when_not_active():
    player = HoldemPlayer(stack=100)
    player.is_active = False
    with pytest.raises(ValueError):
        player.bet(1)

def test_holdemplayer_fold_turns_player_inactive():
    player = HoldemPlayer(stack=100)
    player.participate()
    player.fold()
    
    assert player.is_active == False

def test_withdraw_current_bet_returns_current_bet():
    player = HoldemPlayer(stack=100)
    player.participate()
    player.bet(49)

    bet_amount = player.withdraw_current_bet()
    assert bet_amount == 49

def test_withdraw_current_bet_returns_current_bet():
    player = HoldemPlayer(stack=100)

    player.participate()
    player.bet(37)
    player.withdraw_current_bet()

    assert player.current_bet == 0

def test_is_current_bet_zero_returns_correctly():
    player_zero_bet = HoldemPlayer(stack=100)
    player_positive_bet = HoldemPlayer(stack=100)

    player_positive_bet.participate()
    player_positive_bet.bet(34)

    assert player_zero_bet.is_current_bet_zero() == True
    assert player_positive_bet.is_current_bet_zero() == False

def test_get_current_bet_zero_returns_correctly():
    player = HoldemPlayer(stack=100)

    player.participate()
    player.bet(45)

    assert player.get_current_bet() ==  45