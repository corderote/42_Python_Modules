#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    try:
        print(f"Input data is '{temp_str}'")
        print(f"Temperature is now: {input_temperature(temp_str)}ºC")
    except ValueError:
        print(f"Caught input_temperature error: "
              f"Invalid literal for int() with base 10: '{temp_str}'")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")
