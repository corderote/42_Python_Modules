import random
from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"[Fireball] hits {target} for {power} damage"


def blast(target: str, power: int) -> str:
    return f"[Blast] hits {target} for {power} damage"


def check_mana_cost(target: str, mana_cost: int) -> bool:
    if mana_cost < 20 or target == "Dragon":
        return False
    return True


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combine


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], None]:
    def multi_spell(target: str, power: int) -> None:
        for spell in spells:
            print(spell(target, power))
    return multi_spell


if __name__ == "__main__":
    test_values = [12, 9, 25, 15, 23, 32, 5, 1]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight', 'Angel']

    print("\nTesting spell combiner: ...")
    combo = spell_combiner(fireball, blast)
    spell_res = combo(str(random.sample(test_targets, 1)[0]),
                      int(random.sample(test_values, 1)[0]))
    print(f"Combined spell result:\n{spell_res[0]}, {spell_res[1]}")

    print("\nTesting power amplifier: ...")
    values = (str(random.sample(test_targets, 1)[0]),
              int(random.sample(test_values, 1)[0]))
    print(f"Base spell: {fireball(values[0], values[1])}")
    better_fireball = power_amplifier(fireball, 10)
    print(f"Amplified spell: {better_fireball(values[0], values[1])}")

    print("\nTesting conditional caster: ...")
    if_spell = conditional_caster(check_mana_cost, blast)
    print(f"Check valid: {if_spell(test_targets[3], 30)}")
    print(f"Check invalid: {if_spell(test_targets[0], 30)}")
    print(f"Check invalid: {if_spell(test_targets[3], 10)}")

    print("\nTesting spell sequence: ...")
    values = (str(random.sample(test_targets, 1)[0]),
              int(random.sample(test_values, 1)[0]))
    spell_lst: list[Callable[[str, int], str]] = [
        fireball, blast, blast, fireball
    ]
    multispell = spell_sequence(spell_lst)
    print("Casting multispell:")
    multispell(values[0], values[1])

    print("\nAll tests completed.\n")
