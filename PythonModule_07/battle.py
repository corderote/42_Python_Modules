from ex0 import Creature, CreatureFactory, FireFactory, AquaFactory


def factory_test(factory: CreatureFactory) -> None:
    base_c: Creature = factory.create_base()
    evol_c: Creature = factory.create_evolved()
    print(base_c.describe())
    print(base_c.attack())
    print(evol_c.describe())
    print(evol_c.attack())


def battle_test(f1: CreatureFactory, f2: CreatureFactory) -> None:
    c1: Creature = f1.create_base()
    c2: Creature = f2.create_base()
    print(c1.describe())
    print(" vs. ")
    print(c2.describe())
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    print("Testing factory: ")
    factory_test(FireFactory())
    print("\nTesting factory: ")
    factory_test(AquaFactory())
    print("\nTesting battle: ")
    battle_test(FireFactory(), AquaFactory())
