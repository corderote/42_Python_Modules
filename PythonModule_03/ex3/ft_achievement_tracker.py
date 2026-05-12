#!/usr/bin/python3


import random


achievements_set = {'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'}
players = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    nbr = random.randint(0, len(achievements_set))
    player_achievements = random.sample(list(achievements_set), nbr)
    return set(player_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    players_sets = []
    for player in players:
        players_sets.append(gen_player_achievements())
    for idx in range(0, len(players)):
        print(f"Player {players[idx]}: {players_sets[idx]}")
    print()
    print()
    union_set: set[str] = set()
    for items in players_sets:
        union_set = union_set.union(items)
    print(f"All distinct achievements: {union_set}")
    print()
    common_set = union_set
    for items in players_sets:
        common_set = common_set.intersection(items)
    print(f"Common achievements: {common_set}")
    print()
    for idx in range(0, len(players)):
        dif = union_set
        for aux in range(0, len(players)):
            if (aux != idx):
                dif = dif.difference(players_sets[aux])
        print(f"Only {players[idx]} has: {dif}")
    print()
    for idx in range(0, len(players)):
        dif = achievements_set.difference(players_sets[idx])
        print(f"{players[idx]} is missing: {dif}")
