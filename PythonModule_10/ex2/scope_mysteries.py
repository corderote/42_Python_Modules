import random
from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    base_power = initial_power

    def accumulate(addition: int) -> int:
        nonlocal base_power
        base_power += addition
        return base_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    enchantment_types = ['Shocking', 'Radiant', 'Dark']
    items_to_enchant = ['Cloak', 'Amulet', 'Wand', 'Ring']

    print("\nTesting mage counter: ...")
    count_spell_1 = mage_counter()
    count_spell_2 = mage_counter()
    print(f"Mage Counter A [1]: {count_spell_1()}")
    print(f"Mage Counter A [2]: {count_spell_1()}")
    print(f"Mage Counter B: {count_spell_2()}")

    print("\nTesting spell accumulator: ...")
    base_value = 100
    accum_spell = spell_accumulator(base_value)
    random_value = random.randint(20, 50)
    print(f"Base {base_value}, add {random_value}: "
          f"{accum_spell(random_value)}")
    random_value = random.randint(20, 50)
    print(f"Base {base_value}, add {random_value}: "
          f"{accum_spell(random_value)}")

    print("\nTesting enchantment factory: ...")
    random_enchant = str(random.sample(enchantment_types, 1)[0])
    random_weapon = str(random.sample(items_to_enchant, 1)[0])
    enchant = enchantment_factory(random_enchant)
    print(f"{enchant(random_weapon)}")
    random_enchant = str(random.sample(enchantment_types, 1)[0])
    random_weapon = str(random.sample(items_to_enchant, 1)[0])
    enchant = enchantment_factory(random_enchant)
    print(f"{enchant(random_weapon)}")

    print("\nTesting memory vault: ...")
    memory_maker: dict[str, Callable[..., Any]] = memory_vault()
    print("Store 'secret' = 42")
    memory_maker['store']('secret', 42)
    print(f"Recall 'secret': {memory_maker['recall']('secret')}")
    print(f"Recall 'unknown': {memory_maker['recall']('unknown')}")

    print("\nAll tests completed.\n")
