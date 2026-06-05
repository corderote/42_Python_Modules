from ex0 import Creature
from ex0 import CreatureFactory
from .factories import GrassFactory as GrassFactory
from .factories import NormalFactory as NormalFactory
from .capabilities import HealCapability as HealCapability
from .capabilities import TransformCapability as TransformCapability


if __name__ == "__main__":
    f1: CreatureFactory = GrassFactory()
    f2: CreatureFactory = NormalFactory()
    c1: Creature = f1.create_base()
    c2: Creature = f2.create_evolved()
    h: HealCapability
    t: TransformCapability
