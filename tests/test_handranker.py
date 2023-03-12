from models.HandRanker import HandRanker
from models.Card import Card
from models.CardGenerator import generate_cards
import pytest

def test_handranker_raises_error_when_not_initialized_with_5_cards():
    card1, card2, card3, card4, card5, card6 = generate_cards(['2h', '3d', '4d', '5d', '6d', '7d'])

    with pytest.raises(ValueError):
        HandRanker([])
    with pytest.raises(ValueError):
        HandRanker([card1, card2, card3, card4])
    with pytest.raises(ValueError):
        HandRanker([card1, card2, card3, card4, card5, card6])

def test_handranker_raises_error_when_initialized_with_duplicate_cards():
    card1, card2, card3, card4 = generate_cards(['2h', '3d', '4d', '5d'])

    with pytest.raises(ValueError):
        HandRanker([card1, card1, card2, card3, card4])
    with pytest.raises(ValueError):
        HandRanker([card1, card1, card1, card3, card4])
    with pytest.raises(ValueError):
        HandRanker([card1, card1, card1, card1, card4])
    with pytest.raises(ValueError):
        HandRanker([card1, card1, card1, card1, card1])

def test_handranker_is_flush_returns_true_for_all_suits():
    assert HandRanker(generate_cards(['3d', '4d', '5d', '6d', '7d']))._is_flush() == True
    assert HandRanker(generate_cards(['3h', '4h', '5h', '6h', '7h']))._is_flush() == True
    assert HandRanker(generate_cards(['3s', '4s', '5s', '6s', 'as']))._is_flush() == True
    assert HandRanker(generate_cards(['3c', '4c', '5c', '6c', '9c']))._is_flush() == True

def test_handranker_is_flush_returns_false_if_different_suits():
    assert HandRanker(generate_cards(['3c', '4d', '5d', '6d', '7d']))._is_flush() == False
    assert HandRanker(generate_cards(['3c', '4c', '5d', '6d', '7d']))._is_flush() == False
    assert HandRanker(generate_cards(['3c', '4c', '5c', '6d', '7d']))._is_flush() == False
    assert HandRanker(generate_cards(['3c', '4h', '5s', '6c', '7d']))._is_flush() == False

def test_handranker_is_straight_returns_true_when_all_ranks_consecutive():
    assert HandRanker(generate_cards(['ac', '2h', '3s', '4c', '5d']))._is_straight() == True
    assert HandRanker(generate_cards(['2c', '3h', '4s', '5c', '6d']))._is_straight() == True
    assert HandRanker(generate_cards(['3c', '4h', '5s', '6c', '7d']))._is_straight() == True
    assert HandRanker(generate_cards(['ac', 'jh', 'ks', 'qc', 'td']))._is_straight() == True
    assert HandRanker(generate_cards(['9c', 'jh', 'ks', 'qc', 'td']))._is_straight() == True
    assert HandRanker(generate_cards(['9c', 'jh', '8s', 'qc', 'td']))._is_straight() == True

def test_handranker_is_straight_returns_false_when_ranks_not_consecutive():
    assert HandRanker(generate_cards(['9c', '2h', '8s', 'qc', 'td']))._is_straight() == False
    assert HandRanker(generate_cards(['ac', 'jh', 'ks', 'qc', '2d']))._is_straight() == False
    assert HandRanker(generate_cards(['ac', '3h', 'ks', 'qc', '2d']))._is_straight() == False
    assert HandRanker(generate_cards(['9c', '9h', '8s', 'qc', 'td']))._is_straight() == False

def test_handranker_generate_rank_histogram_generates_correctly():
    assert HandRanker(generate_cards(['2c', '3h', '4s', '5c', '6d']))._generate_rank_histogram() == [1, 1, 1, 1, 1]
    assert HandRanker(generate_cards(['2c', '2h', '4s', '5c', '6d']))._generate_rank_histogram() == [2, 1, 1, 1]
    assert HandRanker(generate_cards(['2c', '2h', '4s', '4c', '6d']))._generate_rank_histogram() == [2, 2, 1]
    assert HandRanker(generate_cards(['2c', '2h', '2s', '5c', '6d']))._generate_rank_histogram() == [3, 1, 1]
    assert HandRanker(generate_cards(['2c', '2h', '2s', '5c', '5d']))._generate_rank_histogram() == [3, 2]
    assert HandRanker(generate_cards(['2c', '2h', '2s', '5c', '2d']))._generate_rank_histogram() == [4, 1]

def test_handranker_get_highest_rank_generates_correctly():
    assert HandRanker.get_highest_rank(generate_cards(['2c', '2h', '2s', '5c', '2d'])) == '5'
    assert HandRanker.get_highest_rank(generate_cards(['2c', '2h', 'ts', '5c', '2d'])) == 't'
    assert HandRanker.get_highest_rank(generate_cards(['2c', 'ah', 'as', '5c', '2d'])) == 'a'
    assert HandRanker.get_highest_rank(generate_cards(['2c', 'jh', 'ts', 'jc', 'jd'])) == 'j'

def test_handranker_update_hand_stats_highcard_generates_correctly():
    hr_flush = HandRanker(generate_cards(['3c', '4d', '5c', '6c', '9c']))

    hr_flush.update_hand_stats()

    assert hr_flush.is_hand_flush == False
    assert hr_flush.is_hand_straight == False
    assert hr_flush.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_flush.highest_rank == '9'

def test_handranker_update_hand_stats_flush_generates_correctly():
    hr_flush = HandRanker(generate_cards(['3c', '4c', '5c', '6c', '9c']))

    hr_flush.update_hand_stats()

    assert hr_flush.is_hand_flush == True
    assert hr_flush.is_hand_straight == False
    assert hr_flush.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_flush.highest_rank == '9'

def test_handranker_update_hand_stats_straight_generates_correctly():
    hr_straight = HandRanker(generate_cards(['3c', '4c', '5c', '6c', '7h']))

    hr_straight.update_hand_stats()

    assert hr_straight.is_hand_flush == False
    assert hr_straight.is_hand_straight == True
    assert hr_straight.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_straight.highest_rank == '7'

def test_handranker_update_hand_stats_straight_flush_generates_correctly():
    hr_straight_flush = HandRanker(generate_cards(['3c', '4c', '5c', '6c', '7c']))

    hr_straight_flush.update_hand_stats()

    assert hr_straight_flush.is_hand_flush == True
    assert hr_straight_flush.is_hand_straight == True
    assert hr_straight_flush.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_straight_flush.highest_rank == '7'

def test_handranker_update_hand_stats_pair_generates_correctly():
    hr_pair = HandRanker(generate_cards(['3c', '3h', '5c', '6c', '7c']))

    hr_pair.update_hand_stats()

    assert hr_pair.is_hand_flush == False
    assert hr_pair.is_hand_straight == False
    assert hr_pair.rank_histogram == [2, 1, 1, 1]
    assert hr_pair.highest_rank == '7'

def test_handranker_update_hand_stats_2_pair_generates_correctly():
    hr_2_pair = HandRanker(generate_cards(['3c', '3h', '5c', '5h', '7c']))

    hr_2_pair.update_hand_stats()

    assert hr_2_pair.is_hand_flush == False
    assert hr_2_pair.is_hand_straight == False
    assert hr_2_pair.rank_histogram == [2, 2, 1]
    assert hr_2_pair.highest_rank == '7'

def test_handranker_update_hand_stats_3_of_a_kind_generates_correctly():
    hr_3_kind = HandRanker(generate_cards(['3c', '3h', '3s', '5h', '7c']))

    hr_3_kind.update_hand_stats()

    assert hr_3_kind.is_hand_flush == False
    assert hr_3_kind.is_hand_straight == False
    assert hr_3_kind.rank_histogram == [3, 1, 1]
    assert hr_3_kind.highest_rank == '7'

def test_handranker_update_hand_stats_full_house_generates_correctly():
    hr_full_house = HandRanker(generate_cards(['3c', '3h', '3s', '5h', '5c']))

    hr_full_house.update_hand_stats()

    assert hr_full_house.is_hand_flush == False
    assert hr_full_house.is_hand_straight == False
    assert hr_full_house.rank_histogram == [3, 2]
    assert hr_full_house.highest_rank == '5'

def test_handranker_update_hand_stats_4_of_a_kind_generates_correctly():
    hr_4_kind = HandRanker(generate_cards(['3c', '3h', '3s', '3d', '5c']))

    hr_4_kind.update_hand_stats()

    assert hr_4_kind.is_hand_flush == False
    assert hr_4_kind.is_hand_straight == False
    assert hr_4_kind.rank_histogram == [4, 1]
    assert hr_4_kind.highest_rank == '5'

def test_handranker_get_hand_rank_throws_error_if_stats_not_updated():
    with pytest.raises(Exception):
        HandRanker(generate_cards(['3c', '3h', '3s', '3d', '5c'])).get_hand_rank()

def test_handranker_get_hand_rank_returns_high_card_correctly():
    hr_highcard = HandRanker(generate_cards(['2c', '3h', '4s', '5c', '7d']))

    hr_highcard.update_hand_stats()
    
    assert hr_highcard.get_hand_rank() == "High Card" # change to enum + value