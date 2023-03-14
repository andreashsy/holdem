from models.Rank import Rank
from models.Suit import Suit
from models.HandRank import HandRank

CARD_SUITS = [s.value for s in Suit]
CARD_RANKS = [r.value for r in Rank]
HANDRANKS = [rank.name for rank in HandRank]