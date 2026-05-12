#!/usr/bin/python3

import sys
import typing


def get_file_content(filepath: str) -> str:
    content = ""
    try:
        print(f"Accessing file '{filepath}'")
        file: typing.IO[str] = open(filepath, mode='rt', encoding="utf-8")
        print("---\n")
        content = file.read()
        print(content)
        file.close()
        print(f"\n---\nFile '{filepath}' closed.\n")
    except (OSError, IOError, UnicodeError) as error_msg:
        print(f"Error opening file {filepath}: {error_msg}\n")
    return content


def encode_str(content: str) -> str:
    if content != "":
        print("Transform Data:")
        print("---\n")
        new_content = str.split(content, '\n')
        for line in range(0, len(new_content)):
            new_content[line] += '#'
            print(new_content[line])
        print("\n---\n")
        return '\n'.join(new_content)
    return content


def save_content(content: str) -> None:
    if content != "":
        file_name = input("Enter new file name (or empty): ")
        if file_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{file_name}'")
            try:
                file: typing.IO[str] = open(file_name, mode='wt',
                                            encoding="utf-8")
                file.write(content)
                file.close()
                print(f"Data saved in file '{file_name}'.\n")
            except (OSError, IOError, UnicodeError) as error_msg:
                print(f"Error opening file {file_name}: {error_msg}\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        new_content = encode_str(get_file_content(sys.argv[1]))
        save_content(new_content)
    else:
        print(f"Usage: {sys.argv[0]} <file>")
