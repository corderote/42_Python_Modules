import random
import time
from functools import wraps
from typing import Any, Callable


def spell_timer(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print(f"Casting [{func.__name__.upper()}]: ...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        delta_time = round(end_time - start_time, 3)
        print(f"Spell completed in {delta_time} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power: int = kwargs.get('power', args[-1] if args else 0)
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err_msg:
                    print(err_msg)
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("\nTesting spell timer: ...")

    @spell_timer
    def fireball(power: int) -> str:
        time.sleep(0.101)
        return f"Warlock casted [FIREBALL] at lvl {power}"

    spell_result = fireball(25)
    print(spell_result)

    print("\nTesting power validator: ...")

    @power_validator(min_power=25)
    def blast(power: int) -> str:
        return f"Warlock casted [BLAST] at lvl {power}"

    print(f"BLAST LVL 20: {blast(20)}")
    print(f"BLAST LVL 50: {blast(50)}")

    print("\nTesting retry spell: ...")

    @retry_spell(max_attempts=3)
    def teleport(mana: int) -> str:
        random_check = random.randint(0, 10)
        if mana + random_check <= 10:
            raise ValueError("Warlock failed cast due to mana issues.")
        return "Warlock casted [TELEPORTATION] successfully!"

    print(teleport(2))
    print(teleport(10))

    print("\nTesting spell reducer: ...")
    print(f"Mage name [AI]: {MageGuild.validate_mage_name('Al')}")
    print(f"Mage name [Bot123]: {MageGuild.validate_mage_name('Bot123')}")
    print(f"Mage name [Gandalf]: {MageGuild.validate_mage_name('Gandalf')}")

    mage = MageGuild()
    print(mage.cast_spell("[ELDRICH BLAST]", 5))
    print(mage.cast_spell("[ELDRICH BLAST]", 50))

    print("\nAll tests completed.\n")
