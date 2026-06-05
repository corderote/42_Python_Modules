from ex0 import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self._name = "Sproutling"
        self._type = ["Grass"]
        self._attacks = ["Vine Whip"]
        super().__init__()

    def attack(self) -> str:
        return f"{self._name} uses {self._attacks[0]}!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self._name = "Bloomelle"
        self._type = ["Grass"]
        self._attacks = ["Petal Dance"]
        super().__init__()

    def attack(self) -> str:
        return f"{self._name} uses {self._attacks[0]}!"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self._name = "Shiftling"
        self._type = ["Normal"]
        self._attacks = ["Tackle", "Hyper Beam"]
        self._transformed = False
        super().__init__()

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} uses {self._attacks[1]}!"
        else:
            return f"{self._name} uses {self._attacks[0]}!"

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        self._name = "Morphagon"
        self._type = ["Normal", "Dragon"]
        self._attacks = ["Dragon Pulse", "Draco Meteor"]
        self._transformed = False
        super().__init__()

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} uses {self._attacks[1]}!"
        else:
            return f"{self._name} uses {self._attacks[0]}!"

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."
