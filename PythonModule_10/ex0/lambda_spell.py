from typing import Any
import random


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    powers: list[int] = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    artifacts: list[dict[str, Any]] = [
        {'name': 'Ice Wand', 'power': 115, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 84, 'type': 'weapon'},
        {'name': 'Storm Crown', 'power': 119, 'type': 'focus'},
        {'name': 'Light Prism', 'power': 107, 'type': 'accessory'}
    ]
    mages: list[dict[str, Any]] = [
        {'name': 'Kai', 'power': 82, 'element': 'wind'},
        {'name': 'Jordan', 'power': 100, 'element': 'wind'},
        {'name': 'Rowan', 'power': 97, 'element': 'shadow'},
        {'name': 'Alex', 'power': 92, 'element': 'water'},
        {'name': 'Riley', 'power': 56, 'element': 'shadow'}
    ]
    spells: list[str] = ['blizzard', 'freeze', 'flash', 'darkness']

    print("\nTesting artifact sorter: ...")
    sorted_atifacts: list[dict[str, Any]] = artifact_sorter(artifacts)
    for idx in range(len(sorted_atifacts)):
        print(f"[#{idx}] {sorted_atifacts[idx]['name']} with power: "
              f"{sorted_atifacts[idx]['power']}")

    print("\nTesting power filter: ...")
    min_power: int = random.randint(60, 90)
    mages_filter: list[dict[str, Any]] = power_filter(mages, min_power)
    print(f"Revealing mages with power greater than {min_power}:")
    for mage in mages_filter:
        print(f"- {mage['name']} with power {mage['power']}")

    print("\nTesting spell transformer: ...")
    new_spells = spell_transformer(spells)
    print("New sparkling spells:")
    for spell in new_spells:
        print(f"{spell}")

    print("\nTesting mage stats: ...")
    stats = mage_stats(mages)
    print(f"MAX POWER: {stats['max_power']}\n"
          f"MIN POWER: {stats['min_power']}\n"
          f"AVERAGE: {stats['avg_power']}\n")

    print("\nAll tests completed.\n")
