from models.Deck import Deck

def test_shuffle_deck_is_different_from_unshuffled():
    d = Deck()
    unshuffled_cards = d.get_cards()

    d.shuffle()
    
    assert d.cards != unshuffled_cards

def test_deck_cards_are_unique():
    d = Deck()
    assert len(d.get_cards()) == len(set(d.get_cards()))

    d.shuffle()
    assert len(d.get_cards()) == len(set(d.get_cards()))

def test_deck_has_52_cards():
    d = Deck()
    assert d.size() == 52

    d.shuffle()
    assert d.size() == 52

def test_draw_card_reduces_deck_by_one():
    d = Deck()
    num_before_draw = d.size()
    d.draw_card()
    assert d.size() == num_before_draw - 1

def test_draw_card_draws_last_card():
    d = Deck()
    d.shuffle()

    deck_before = d.get_cards()
    d.draw_card()
    deck_after = d.get_cards()

    assert deck_after == deck_before[:-1]