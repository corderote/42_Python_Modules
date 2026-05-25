def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    check = validate_ingredients(ingredients)
    if "INVALID" in check:
        return f"Spell rejected: {spell_name} ({check})"
    else:
        return f"Spell recorded: {spell_name} ({check})"
