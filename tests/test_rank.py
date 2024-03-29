import pytest
from models.Rank import Rank

def test_rank_raises_error_when_compared_with_non_ranks():
    with pytest.raises(NotImplementedError):
        Rank('a') > 1
    with pytest.raises(NotImplementedError):
        Rank('a') > 'a'
    with pytest.raises(NotImplementedError):
        Rank('a') < None
    with pytest.raises(NotImplementedError):
        Rank('a') < False

def test_rank_can_be_ordered():
    assert Rank('a') > Rank('k')
    assert Rank('k') > Rank('q')
    assert Rank('q') > Rank('j')
    assert Rank('j') > Rank('t')
    assert Rank('t') > Rank('9')
    assert Rank('9') > Rank('8')
    assert Rank('8') > Rank('7')
    assert Rank('7') > Rank('6')
    assert Rank('6') > Rank('5')
    assert Rank('5') > Rank('4')
    assert Rank('4') > Rank('3')
    assert Rank('3') > Rank('2')