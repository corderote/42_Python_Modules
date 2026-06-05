#!/usr/bin/python3

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", end="")
    print(alchemy.create_air())
    try:
        print("Now show that not all functions can be reached.")
        print("This will raise an exception!")
        print("Testing the hidden create_earth: ", end="")
        print(alchemy.create_earth())
    except ImportError as err_msg:
        print(err_msg)
