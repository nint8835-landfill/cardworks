from typing import Union

from . import Player


class Card(object):
    """
    Base class representing a card that can be played during a game.
    """

    owner: Player = None

    name: str = "Unnamed Card"
    description: str = "No description specified."

    def on_play(self):
        """
        Called when this card is played.
        """
        pass

    def on_play_other(self, other: Card):
        """
        Called when another card is played while this card is in a player's hand or on the board.
        :param other: The card that was played.
        """
        pass


class Creature(Card):
    """
    Represents a creature that can be placed on the board.
    """

    attack: int = 0
    health: int = 0

    def on_attack(self, target: Union[Creature, Player]):
        """
        Called when this creature targets either another creature or a player.
        :param target: The target that this creature is attacking.
        """

        if isinstance(target, Player):
            for card in target.board:
                card.on_attacked(self)
        else:
            target.on_attacked(self)

    def on_attacked(self, attacker: Creature):
        """
        Called when this creature is attacked by another creature.
        :param attacker: The creature that is attacking.
        """
        self.health -= attacker.attack
        if self.health <= 0:
            self.on_destroyed()

    def on_destroyed(self):
        """
        Called when this card is destroyed
        """
        self.owner.board.remove(self)
        self.owner.graveyard.append(self)
