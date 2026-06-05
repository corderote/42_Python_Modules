from .creatures import Creature as Creature
from .factories import CreatureFactory as CreatureFactory
from .factories import FireFactory as FireFactory
from .factories import AquaFactory as AquaFactory


if __name__ == "__main__":
    f1: CreatureFactory = FireFactory()
    f2: CreatureFactory = AquaFactory()
    c1: Creature = f1.create_base()
    c2: Creature = f2.create_evolved()
