#!/usr/bin/python3

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            13/0
        case 2:
            open("/non/existent/file")
        case 3:
            "str" + 123
    return


def test_error_types() -> None:
    for op_nbr in range(0, 5, 1):
        print(f"Testing operation {op_nbr}...")
        try:
            garden_operations(op_nbr)
            print("Operation completed successfully.")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as error_msg:
            print(f"Caught {error_msg.__class__.__name__}: {error_msg} ")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
