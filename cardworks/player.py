from typing import List

from . import Card, Creature

class Player(object):
    """
    Represents a player in a game.
    """

    board: List[Creature] = []
    deck: List[Card] = []
    hand: List[Card] = []
    graveyard: List[Card] = []

    health: int = 30
