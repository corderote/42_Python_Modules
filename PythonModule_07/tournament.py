from ex0 import (Creature, CreatureFactory,
                 FireFactory, AquaFactory)
from ex1 import (NormalFactory, GrassFactory)
from ex2 import (BattleStrategy, BattleError,
                 NormalStrategy, AggressiveStrategy, DefensiveStrategy)


def single_battle(lst: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("\n*** Tournament ***")
    print(f"{len(lst)} oponents involved.")
    try:
        for idx_1 in range(0, len(lst)):
            for idx_2 in range(idx_1 + 1, len(lst)):
                print("\n* Battle *")
                c1: Creature = lst[idx_1][0].create_base()
                c2: Creature = lst[idx_2][0].create_base()
                print(f"{c1.describe()}\n vs. \n{c2.describe()}")
                print(" now fight! ")
                lst[idx_1][1].act(c1)
                lst[idx_2][1].act(c2)
    except BattleError as err_msg:
        print(f"Battle error, aborting tournament: {err_msg}\n")


if __name__ == "__main__":
    normal: BattleStrategy = NormalStrategy()
    aggro: BattleStrategy = AggressiveStrategy()
    defense: BattleStrategy = DefensiveStrategy()
    print("\nTournament 0 (basic)\n"
          "[(Flameling+Normal),(Sproutling+Defensive)]")
    single_battle([(FireFactory(), normal), (GrassFactory(), defense)])
    print("\nTournament 1 (error)\n"
          "[(Flameling+Aggresive),(Sproutling+Defensive)]")
    single_battle([(FireFactory(), aggro), (GrassFactory(), defense)])
    print("\nTournament 2 (multiple)\n"
          "[(Flameling+Normal),(Sproutling+Defensive),(Shiftling+Aggresive)]")
    single_battle([(AquaFactory(), normal),
                   (GrassFactory(), defense),
                   (NormalFactory(), aggro)])
