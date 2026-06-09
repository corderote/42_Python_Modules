from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any
import operator
import random


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops: dict[str, Callable[..., int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"[ERROR] Unknown operation: {operation}")
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, partial[str]]:
    return {
        'eldrich': partial(base_enchantment, 50, "eldrich"),
        'fire': partial(base_enchantment, 50, "fire"),
        'ice': partial(base_enchantment, 50, "ice")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 1:
        return 0
    if n < 3:
        return 1
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(value: Any) -> str:
        return "[Dispatch WARN] Not supported type."

    @dispatch.register(int)
    def d_int(value: int) -> str:
        return f"Hit for {value} points of damage"

    @dispatch.register(str)
    def d_str(value: str) -> str:
        return f"Casting {value} enchanment"

    @dispatch.register(list)
    def d_lst(value: list[str | int]) -> str:
        string = f"{len(value)} spells"
        for item in value:
            string += f"\n{dispatch(item)}"
        return string
    return dispatch


if __name__ == "__main__":
    spell_powers = random.sample(range(10, 50), 5)
    operations = ['add', 'multiply', 'max', 'min', 'invalid']
    fibonacci_tests = [10, 21, 42]

    print("\nTesting spell reducer: ...")
    print(f"SPELL POWERS: {spell_powers}")
    for op in operations:
        try:
            print(f"{op.upper()}: {spell_reducer(spell_powers, op)}")
        except ValueError as err_msg:
            print(f"{op.upper()}: {err_msg}")

    print("\nTesting partial enchanter: ...")

    def blast(power: int, element: str, target: str) -> str:
        return (f"[{element.capitalize()} Blast] "
                f"hits {target} for {power} damage")

    enchants = partial_enchanter(blast)
    print(enchants['eldrich']("Mage"))
    print(enchants['fire']("Knight"))
    print(enchants['ice']("Goblin"))

    print("\nTesting memoized fibonacci: ...")
    for number in fibonacci_tests:
        print(memoized_fibonacci(number))
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher: ...")
    spell = spell_dispatcher()
    print(f"INT: {spell(42)}")
    print(f"STR: {spell('glacial')}")
    print(f"LIST: {spell([1, 5, 'fire', 3, 'ice'])}")
    print(f"INVALID: {spell({'invalid': 42})}")

    print("\nAll tests completed.\n")
