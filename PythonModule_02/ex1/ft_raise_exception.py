#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature(temp_str: str) -> None:
    try:
        print(f"Input data is '{temp_str}'")
        print(f"Temperature is now: {input_temperature(temp_str)}ºC")
    except ValueError as error_msg:
        print(f"Caught input_temperature error: {error_msg}")
        return


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
