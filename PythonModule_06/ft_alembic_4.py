#!/usr/bin/python3

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", end="")
    alchemy.create_air()
    try:
        print("Testing the hidden create_earth: ", end="")
        print(alchemy.create_earth())
    except ImportError as err_msg:
        print(err_msg)
