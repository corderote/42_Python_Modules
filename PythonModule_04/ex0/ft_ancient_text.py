#!/usr/bin/python3

import sys


def print_file_content(filepath: str) -> None:
	try:
		print(f"Accessing file '{sys.argv[1]}'")
		file = open(filepath, mode='rt', encoding="utf-8")
		print(f"---\n")
		print(file.read())
		file.close()
		print(f"\n---\nFile '{filepath}' closed.")
	except (OSError, IOError, UnicodeError) as error_msg:
		print(f"Error opening file {filepath}: {error_msg}")


if __name__ == "__main__":
	if len(sys.argv) == 2:
		print("=== Cyber Archives Recovery ===")
		print_file_content(sys.argv[1])
		print()
	pass
