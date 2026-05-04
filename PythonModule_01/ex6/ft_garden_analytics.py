#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name.lower().title()
        self._height = height
        self._days = days
        self._growth_rate = growth_rate
        self._statistics = self.Statistics()
        self.show()

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self._height, 1)}cm, {self._days} days old.")
        self._statistics._show_count += 1

    def grow(self, growth: float = -1.0) -> None:
        if growth < 0:
            self._height = round(self._height + self._growth_rate, 1)
        else:
            self._height = round(self._height + growth, 1)
        self._statistics._grow_count += 1

    def age(self, days: int = 1) -> None:
        self._days += days
        self._statistics._age_count += 1

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative.\n"
                  "Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {round(self._height, 1)}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative.\n"
                  "Age update rejected")
        else:
            self._days = new_age
            print(f"Age updated: {self._days} days")

    def get_age(self) -> float:
        return self._days

    def status(self) -> None:
        print(f"Current state: {self.name}: "
              f"{round(self._height, 1)}cm, {self._days} days old.")

    def statistics(self) -> None:
        self._statistics.show()

    @staticmethod
    def older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class Statistics():
        def __init__(self) -> None:
            self._show_count = 0
            self._age_count = 0
            self._grow_count = 0

        def show(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 color: str, bloomed: bool = False,
                 growth_rate: float = 1.0) -> None:
        self._color = color
        self._bloomed = bloomed
        super().__init__(name, height, days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        if not self._bloomed:
            self._bloomed = True
        else:
            print("ERROR: Flower already bloomed.")


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 color: str, bloomed: bool = False,
                 growth_rate: float = 1.0) -> None:
        self._seeds = 0
        super().__init__(name, height, days, color, bloomed, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self, seeds: int = 10) -> None:
        super().bloom()
        self._seeds = seeds


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int,
                 diameter: float, growth_rate: float = 1.0) -> None:
        self._trunk_diameter = diameter
        self._statistics: Tree.Statistics = self.Statistics()
        super().__init__(name, height, days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}c wide.")
        self._statistics._shade_count += 1

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            self._shade_count = 0
            super().__init__()

        def show(self) -> None:
            super().show()
            print(f" {self._shade_count} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str, nutritional_value: float = 0.0,
                 growth_rate: float = 1.0) -> None:
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        super().__init__(name, height, days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {round(self._nutritional_value)}")

    def age(self, value: float = 0.5) -> None:
        super().age()
        self._nutritional_value += value

    def grow(self, value: float = 0.5) -> None:
        super().grow()
        self._nutritional_value += value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Check year-old")
    days = 30
    print(f"Is {days} days more than a year? -> {Plant.older_than_year(days)}")
    days = 400
    print(f"Is {days} days more than a year? -> {Plant.older_than_year(days)}")
    print()
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    print(f"[statistics for {flower.name.lower()}]")
    flower.statistics()
    print(f"[asking the {flower.name.lower()} to bloom]")
    flower.grow(8.0)
    flower.bloom()
    flower.show()
    print(f"[statistics for {flower.name.lower()}]")
    flower.statistics()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    print(f"[statistics for {tree.name.lower()}]")
    tree.statistics()
    print(f"[asking the {tree.name.lower()} to produce shade]")
    tree.produce_shade()
    print(f"[statistics for {tree.name.lower()}]")
    tree.statistics()
    print()
    seed = Seed("Sunflower", 80.0, 45, "yellow", growth_rate=1.5)
    print(f"[statistics for {seed.name.lower()}]")
    seed.statistics()
    print(f"[make {seed.name.lower()} grow, age and bloom]")
    days = 20
    seed.grow(30.0)
    seed.age(20)
    seed.bloom(42)
    seed.show()
    print(f"[statistics for {seed.name.lower()}]")
    seed.statistics()
    print()
    print("=== Anonymous")
    plant = Plant.anonymous()
    print(f"[statistics for {plant.name.lower()}]")
    plant.statistics()
