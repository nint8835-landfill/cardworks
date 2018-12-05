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

    def on_attacked(self, attacker: Creature):
        """
        Called when this creature is attacked by another creature.
        :param attacker: The creature that is attacking.
        """
        self.health -= attacker.attack
