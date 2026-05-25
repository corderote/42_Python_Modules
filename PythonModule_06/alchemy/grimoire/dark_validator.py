from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid = True
    ingr_lst = ingredients.split(" ")
    for ingredient in ingr_lst:
        if ingredient not in dark_spell_allowed_ingredients():
            valid = False
    if not valid or len(ingr_lst) == 0:
        return f"{ingredients} - INVALID"
    else:
        return f"{ingredients} - VALID"
