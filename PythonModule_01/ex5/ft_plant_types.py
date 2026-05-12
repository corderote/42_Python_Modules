#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name.lower().title()
        self._height = height
        self._days = days
        self._growth_rate = growth_rate
        self.show()

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self._height, 1)}cm, {self._days} days old.")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._days += 1

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


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int,
                 diameter: float, growth_rate: float = 1.0) -> None:
        self._trunk_diameter = diameter
        super().__init__(name, height, days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}c wide.")


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
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    print(f"[asking the {flower.name.lower()} to bloom]")
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    print(f"[asking the {tree.name.lower()} to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegie = Vegetable("Tomato", 5.0, 10, "April")
    days = 20
    print(f"[make {vegie.name.lower()} grow and age for {days} days]")
    for day in range(0, days, 1):
        vegie.grow()
        vegie.age()
    vegie.show()
    print()
