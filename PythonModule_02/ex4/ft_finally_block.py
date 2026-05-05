#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, msg="Unknown garden error.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PlantError(GardenError):
    def __init__(self, msg="Unknown plant error.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(F"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f" Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_list: list = []) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            water_plant(plant)
    except GardenError as error_msg:
        print(f"Caught {error_msg.__class__.__name__}: {error_msg} ")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print()
    print("Cleanup always happens, even with errors!")
