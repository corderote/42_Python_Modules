#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name
        self.height = height
        self.days = days
        self._growth_rate = growth_rate
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old.")

    def grow(self) -> None:
        self.height = round(self.height + self._growth_rate, 1)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Rose", 25.0, 30)
    Plant("Oak", 200.0, 365)
    Plant("Cactus", 15.0, 120)
    Plant("Sunflower", 80.0, 45)
    Plant("Fern", 15.0, 120)
