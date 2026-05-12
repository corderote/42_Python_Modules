#!/usr/bin/python3


def secure_archive(fp: str, mode: str, content: str = "") -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(fp, mode, encoding="utf-8") as file:
                content = file.read()
            return (True, content)
        elif mode == "w":
            with open(fp, mode, encoding="utf-8") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "ERROR: secure_archive() -> Non valid 'mode'")
    except (OSError, IOError, UnicodeError) as error_msg:
        content = f"{error_msg}"
        return (False, content)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    content = secure_archive("/not/existing/file", "r")
    print(content)
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    content = secure_archive("/etc/master.passwd", "r")
    print(content)
    print("\nUsing 'secure_archive' to read from a regular file:")
    content = secure_archive("ancient_fragment.txt", "r")
    print(content)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", content[1]))
