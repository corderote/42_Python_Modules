#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name.lower().title()
        self._height = height
        self._days = days
        self._growth_rate = growth_rate
        print("Created: ", end="")
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print()
    plant.set_height(25.0)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-1)
    print()
    plant.status()
