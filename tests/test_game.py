import pytest

from models.Game import HoldemGameState
from models.Player import HoldemPlayer

def test_holdemgamestate_raises_if_initialised_with_less_than_2_players():
    with pytest.raises(ValueError):
        HoldemGameState(players=[])
    # with pytest.raises(ValueError):
    #     HoldemGameState(players=[HoldemPlayer()])

