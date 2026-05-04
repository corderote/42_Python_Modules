#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name
        self.height = height
        self.days = days
        self._growth_rate = growth_rate
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old.")

    def grow(self) -> None:
        self.height = round(self.height + self._growth_rate, 1)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant = Plant("Rose", 25.0, 30, 0.8)
    h_start = plant.height
    for day in range(1, 8, 1):
        print(f"=== Day {day} ===")
        plant.age()
        plant.grow()
        plant.show()
    print(f"Growth this week: {round(plant.height - h_start, 1)}cm")
