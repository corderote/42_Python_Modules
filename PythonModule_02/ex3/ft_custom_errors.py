#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error.") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error.") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown water error.") -> None:
        super().__init__(msg)


def test_error_types() -> None:
    for op_nbr in range(0, 5, 1):
        try:
            match int(op_nbr):
                case 0:
                    print("\nTesting PlantError...")
                    raise PlantError("The tomato plant is wilting!")
                case 1:
                    print("\nTesting PlantError...")
                    raise WaterError("Not enough water in the tank!")
                case 2:
                    print("\nTesting catching all garden errors...")
                    raise GardenError("The tomato plant is wilting!")
                case 3:
                    raise GardenError("Not enough water in the tank!")
        except GardenError as error_msg:
            print(f"Caught {error_msg.__class__.__name__}: {error_msg} ")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_error_types()
    print("\nAll custom error types work correctly!")
