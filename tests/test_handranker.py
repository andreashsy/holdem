import pytest
from models.HandRanker import HandRanker
from models.HandRank import HandRank
from models.CardGenerator import generate_cards
from models.Rank import Rank

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

def test_handranker_find_highest_rank_generates_correctly():
    assert HandRanker.find_highest_rank(generate_cards(['2c', '2h', '2s', '5c', '2d'])) == Rank('5')
    assert HandRanker.find_highest_rank(generate_cards(['2c', '2h', 'ts', '5c', '2d'])) == Rank('t')
    assert HandRanker.find_highest_rank(generate_cards(['2c', 'ah', 'as', '5c', '2d'])) == Rank('a')
    assert HandRanker.find_highest_rank(generate_cards(['2c', 'jh', 'ts', 'jc', 'jd'])) == Rank('j')

def test_handranker_update_hand_stats_highcard_generates_correctly():
    hr_flush = HandRanker(generate_cards(['3c', '4d', '5c', '6c', '9c']))

    hr_flush.update_hand_stats()

    assert hr_flush.is_hand_flush == False
    assert hr_flush.is_hand_straight == False
    assert hr_flush.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_flush.highest_rank == Rank('9')

def test_handranker_update_hand_stats_flush_generates_correctly():
    hr_flush = HandRanker(generate_cards(['3c', '4c', '5c', '6c', '9c']))

    hr_flush.update_hand_stats()

    assert hr_flush.is_hand_flush == True
    assert hr_flush.is_hand_straight == False
    assert hr_flush.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_flush.highest_rank == Rank('9')

def test_handranker_update_hand_stats_straight_generates_correctly():
    hr_straight = HandRanker(generate_cards(['3c', '4c', '5c', '6c', '7h']))

    hr_straight.update_hand_stats()

    assert hr_straight.is_hand_flush == False
    assert hr_straight.is_hand_straight == True
    assert hr_straight.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_straight.highest_rank == Rank('7')

def test_handranker_update_hand_stats_straight_flush_generates_correctly():
    hr_straight_flush = HandRanker(generate_cards(['3c', '4c', '5c', '6c', '7c']))

    hr_straight_flush.update_hand_stats()

    assert hr_straight_flush.is_hand_flush == True
    assert hr_straight_flush.is_hand_straight == True
    assert hr_straight_flush.rank_histogram == [1, 1, 1, 1, 1]
    assert hr_straight_flush.highest_rank == Rank('7')

def test_handranker_update_hand_stats_pair_generates_correctly():
    hr_pair = HandRanker(generate_cards(['3c', '3h', '5c', '6c', '7c']))

    hr_pair.update_hand_stats()

    assert hr_pair.is_hand_flush == False
    assert hr_pair.is_hand_straight == False
    assert hr_pair.rank_histogram == [2, 1, 1, 1]
    assert hr_pair.highest_rank == Rank('7')

def test_handranker_update_hand_stats_2_pair_generates_correctly():
    hr_2_pair = HandRanker(generate_cards(['3c', '3h', '5c', '5h', '7c']))

    hr_2_pair.update_hand_stats()

    assert hr_2_pair.is_hand_flush == False
    assert hr_2_pair.is_hand_straight == False
    assert hr_2_pair.rank_histogram == [2, 2, 1]
    assert hr_2_pair.highest_rank == Rank('7')

def test_handranker_update_hand_stats_3_of_a_kind_generates_correctly():
    hr_3_kind = HandRanker(generate_cards(['3c', '3h', '3s', '5h', '7c']))

    hr_3_kind.update_hand_stats()

    assert hr_3_kind.is_hand_flush == False
    assert hr_3_kind.is_hand_straight == False
    assert hr_3_kind.rank_histogram == [3, 1, 1]
    assert hr_3_kind.highest_rank == Rank('7')

def test_handranker_update_hand_stats_full_house_generates_correctly():
    hr_full_house = HandRanker(generate_cards(['3c', '3h', '3s', '5h', '5c']))

    hr_full_house.update_hand_stats()

    assert hr_full_house.is_hand_flush == False
    assert hr_full_house.is_hand_straight == False
    assert hr_full_house.rank_histogram == [3, 2]
    assert hr_full_house.highest_rank == Rank('5')

def test_handranker_update_hand_stats_4_of_a_kind_generates_correctly():
    hr_4_kind = HandRanker(generate_cards(['5c', '3h', '3s', '3d', '3c']))

    hr_4_kind.update_hand_stats()

    assert hr_4_kind.is_hand_flush == False
    assert hr_4_kind.is_hand_straight == False
    assert hr_4_kind.rank_histogram == [4, 1]
    assert hr_4_kind.highest_rank == Rank('5')

def test_handranker_calculate_hand_rank_throws_error_if_stats_not_updated():
    with pytest.raises(Exception):
        HandRanker(generate_cards(['3c', '3h', '3s', '3d', '5c']))._calculate_hand_rank()

def test_handranker_calculate_hand_rank_returns_high_card_correctly():
    hr_highcard = HandRanker(generate_cards(['2c', '3h', '4s', '5c', '7d']))

    hr_highcard.update_hand_stats()
    
    assert hr_highcard._calculate_hand_rank() == HandRank.HIGH_CARD

def test_handranker_calculate_hand_rank_returns_pair_correctly():
    hr_pair = HandRanker(generate_cards(['2c', '2h', '4s', '5c', '7d']))

    hr_pair.update_hand_stats()
    
    assert hr_pair._calculate_hand_rank() == HandRank.PAIR

def test_handranker_calculate_hand_rank_returns_2_pairs_correctly():
    hr_2_pairs = HandRanker(generate_cards(['2c', '2h', '5s', '5c', '7d']))

    hr_2_pairs.update_hand_stats()
    
    assert hr_2_pairs._calculate_hand_rank() == HandRank.TWO_PAIRS

def test_handranker_calculate_hand_rank_returns_3_of_a_kind_correctly():
    hr_3_of_a_kind = HandRanker(generate_cards(['2c', '2h', '2s', '5c', '7d']))

    hr_3_of_a_kind.update_hand_stats()
    
    assert hr_3_of_a_kind._calculate_hand_rank() == HandRank.THREE_OF_A_KIND

def test_handranker_calculate_hand_rank_returns_straight_correctly():
    hr_straight = HandRanker(generate_cards(['2c', '3h', '4s', '5c', '6d']))

    hr_straight.update_hand_stats()
    
    assert hr_straight._calculate_hand_rank() == HandRank.STRAIGHT

def test_handranker_calculate_hand_rank_returns_flush_correctly():
    hr_flush = HandRanker(generate_cards(['2c', '3c', '4c', '5c', '7c']))

    hr_flush.update_hand_stats()
    
    assert hr_flush._calculate_hand_rank() == HandRank.FLUSH

def test_handranker_calculate_hand_rank_returns_full_house_correctly():
    hr_full_house = HandRanker(generate_cards(['2c', '2h', '2s', '7c', '7d']))

    hr_full_house.update_hand_stats()
    
    assert hr_full_house._calculate_hand_rank() == HandRank.FULL_HOUSE

def test_handranker_calculate_hand_rank_returns_4_of_a_kind_correctly():
    hr_4_of_a_kind = HandRanker(generate_cards(['2c', '2h', '2s', '5c', '2d']))

    hr_4_of_a_kind.update_hand_stats()
    
    assert hr_4_of_a_kind._calculate_hand_rank() == HandRank.FOUR_OF_A_KIND

def test_handranker_calculate_hand_rank_returns_straight_flush_correctly():
    hr_straight_flush = HandRanker(generate_cards(['2c', '3c', '4c', '5c', '6c']))

    hr_straight_flush.update_hand_stats()
    
    assert hr_straight_flush._calculate_hand_rank() == HandRank.STRAIGHT_FLUSH

def test_handranker_calculate_hand_rank_returns_royal_flush_correctly():
    hr_royal_flush = HandRanker(generate_cards(['ac', 'jc', 'kc', 'tc', 'qc']))

    hr_royal_flush.update_hand_stats()
    
    assert hr_royal_flush._calculate_hand_rank() == HandRank.ROYAL_FLUSH

def test_handranker_calculate_hand_value_returns_high_card_correctly():
    hr_highcard = HandRanker(generate_cards(['2c', '3h', '4s', '5c', '7d']))

    hr_highcard.update_hand_stats()
    
    assert hr_highcard.calculate_hand_value() == 1.0604030201

def test_handranker_calculate_hand_value_returns_pair_correctly():
    hr_pair = HandRanker(generate_cards(['2c', '2h', '4s', '5c', '7d']))

    hr_pair.update_hand_stats()
    
    assert hr_pair.calculate_hand_value() == 2.01060403

def test_handranker_calculate_hand_value_returns_2_pair_correctly():
    hr_2_pairs = HandRanker(generate_cards(['2c', '2h', '5s', '5c', '7d']))

    hr_2_pairs.update_hand_stats()
    
    assert hr_2_pairs.calculate_hand_value() == 3.040106

def test_handranker_calculate_hand_value_returns_3_of_a_kind_correctly():
    hr_3_of_a_kind = HandRanker(generate_cards(['2c', '2h', '2s', '5c', '7d']))

    hr_3_of_a_kind.update_hand_stats()
    
    assert hr_3_of_a_kind.calculate_hand_value() == 4.010604

def test_handranker_calculate_hand_value_returns_straight_correctly():
    hr_straight = HandRanker(generate_cards(['2c', '3h', '4s', '5c', '6d']))

    hr_straight.update_hand_stats()
    
    assert hr_straight.calculate_hand_value() == 5.05

def test_handranker_calculate_hand_value_returns_flush_correctly():
    hr_flush = HandRanker(generate_cards(['2c', '3c', '4c', '5c', '7c']))

    hr_flush.update_hand_stats()
    
    assert hr_flush.calculate_hand_value() == 6.0604030201

def test_handranker_calculate_hand_value_returns_full_house_correctly():
    hr_full_house = HandRanker(generate_cards(['2c', '2h', '2s', '7c', '7d']))

    hr_full_house.update_hand_stats()
    
    assert hr_full_house.calculate_hand_value() == 7.0106

def test_handranker_calculate_hand_value_returns_4_of_a_kind_correctly():
    hr_4_of_a_kind = HandRanker(generate_cards(['2c', '2h', '2s', '5c', '2d']))

    hr_4_of_a_kind.update_hand_stats()
    
    assert hr_4_of_a_kind.calculate_hand_value() == 8.0104

def test_handranker_calculate_hand_value_returns_straight_flush_correctly():
    hr_straight_flush = HandRanker(generate_cards(['2c', '3c', '4c', '5c', '6c']))

    hr_straight_flush.update_hand_stats()
    
    assert hr_straight_flush.calculate_hand_value() == 9.05

def test_handranker_calculate_hand_value_returns_royal_flush_correctly():
    hr_royal_flush = HandRanker(generate_cards(['ac', 'jc', 'kc', 'tc', 'qc']))

    hr_royal_flush.update_hand_stats()
    
    assert hr_royal_flush.calculate_hand_value() == 10.0
