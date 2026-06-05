from ex0 import Creature, CreatureFactory
from .creatures import (Sproutling, Bloomelle,
                        Shiftling,  Morphagon)


class GrassFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class NormalFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
