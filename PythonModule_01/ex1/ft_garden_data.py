#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old.")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30)
    Plant("Sunflower", 80, 45)
    Plant("Cactus", 15, 120)
