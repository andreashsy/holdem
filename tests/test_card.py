from models.Card import Card
import pytest 

def test_card_raises_error_when_initialized_with_invalid_parameters():
    with pytest.raises(ValueError):
        Card('invalid_value','h')
    with pytest.raises(ValueError):
        Card('2','invalid_value')