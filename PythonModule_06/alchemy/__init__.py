#!/usr/bin/python3

from .elements import create_air as create_air
from .potions import strength_potion as strength_potion
from .potions import healing_potion as heal
from .transmutation.recipes import lead_to_gold as lead_to_gold


if __name__ == "__main__":
    create_air()
    strength_potion()
    heal()
    lead_to_gold()
