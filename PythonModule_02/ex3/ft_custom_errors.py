#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, msg="Unknown garden error.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PlantError(GardenError):
    def __init__(self, msg="Unknown plant error.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class WaterError(GardenError):
    def __init__(self, msg="Unknown water error.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


def test_error_types():
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
