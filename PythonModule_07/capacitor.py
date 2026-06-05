from typing import cast
from ex0 import Creature, CreatureFactory
from ex1 import (GrassFactory, NormalFactory,
                 HealCapability, TransformCapability)


if __name__ == "__main__":

    print("Testing Creature with healing capability.\n base:")
    f1: CreatureFactory = GrassFactory()
    c1: Creature = f1.create_base()
    print(c1.describe())
    print(c1.attack())
    print(cast(HealCapability, c1).heal())
    print(" evolved: ")
    c1 = f1.create_evolved()
    print(c1.describe())
    print(c1.attack())
    print(cast(HealCapability, c1).heal())
    print("\nTesting Creature with transform capability.\n base:")
    f2: CreatureFactory = NormalFactory()
    c2: Creature = f2.create_base()
    print(c2.describe())
    print(c2.attack())
    print(cast(TransformCapability, c2).transform())
    print(c2.attack())
    print(cast(TransformCapability, c2).revert())
    print("evolved: ")
    c2 = f2.create_evolved()
    print(c2.describe())
    print(c2.attack())
    print(cast(TransformCapability, c2).transform())
    print(c2.attack())
    print(cast(TransformCapability, c2).revert())
