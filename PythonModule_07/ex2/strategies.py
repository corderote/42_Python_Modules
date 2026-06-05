from abc import ABC, abstractmethod
from typing import cast
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class BattleError(Exception):
    def __init__(self, msg: str = "Unknown battle error.") -> None:
        super().__init__(msg)


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, critter: Creature) -> bool:
        pass

    def act(self, critter: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, critter: Creature) -> bool:
        try:
            critter.describe()
            critter.attack()
            return True
        except AttributeError:
            return False

    def act(self, critter: Creature) -> None:
        if self.is_valid(critter):
            print(critter.attack())
        else:
            raise BattleError(f"Invalid Creature {critter.__class__.__name__}"
                              " for this strategy")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, critter: Creature) -> bool:
        try:
            critter.describe()
            critter.attack()
            cast(TransformCapability, critter).transform()
            cast(TransformCapability, critter).revert()
            return True
        except AttributeError:
            return False

    def act(self, critter: Creature) -> None:
        if self.is_valid(critter):
            print(cast(TransformCapability, critter).transform())
            print(critter.attack())
            print(cast(TransformCapability, critter).revert())
        else:
            raise BattleError(f"Invalid Creature {critter.__class__.__name__}"
                              " for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, critter: Creature) -> bool:
        try:
            critter.describe()
            critter.attack()
            cast(HealCapability, critter).heal()
            return True
        except AttributeError:
            return False

    def act(self, critter: Creature) -> None:
        if self.is_valid(critter):
            print(critter.attack())
            print(cast(HealCapability, critter).heal())
        else:
            raise BattleError(f"Invalid Creature {critter.__class__.__name__}"
                              " for this deffensive strategy")
