#!/usr/bin/python3

import sys

if __name__ == "__main__":
    idx = 1
    print("=== Command Quest ===")
    print(f"Program Name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Argumments recieved: {len(sys.argv) - 1}")
    else:
        print("No arguments provided!")
    while (idx < len(sys.argv)):
        print(f"Argument {idx}: {sys.argv[idx]}")
        idx += 1
    print(f"Total arguments: {len(sys.argv)}\n")
