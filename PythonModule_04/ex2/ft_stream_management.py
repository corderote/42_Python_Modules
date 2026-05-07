#!/usr/bin/python3

import sys


def get_file_content(filepath: str) -> str:
	content = None
	try:
		sys.stdout.write(f"Accessing file '{filepath}'\n")
		file = open(filepath, mode='rt', encoding="utf-8")
		sys.stdout.write(f"---\n\n")
		content = file.read()
		sys.stdout.write(content)
		file.close()
		sys.stdout.write(f"\n\n---\nFile '{filepath}' closed.\n\n")
	except (OSError, IOError, UnicodeError) as error_msg:
		sys.stderr.write(f"[STDERR] Error opening file {filepath}: {error_msg}\n\n")
	return content


def encode_str(content: str) -> str:
	if content:
		sys.stdout.write("Transform Data:\n")
		sys.stdout.write(f"---\n\n")
		new_content = str.split(content, '\n')
		for line in range(0, len(new_content)):
			new_content[line] += '#\n'
			sys.stdout.write(new_content[line])
		sys.stdout.write(f"\n---\n")
		return '\n'.join(new_content)


def save_content(content: str) -> None:
	if content:
		sys.stdout.write(f"Enter new file name (or empty): ")
		sys.stdout.flush()
		file_name = sys.stdin.readline().strip('\n')
		if file_name == "":
			sys.stdout.write("Not saving data.\n\n")
		else:
			sys.stdout.write(f"Saving data to '{file_name}'\n")
			try:
				file = open(file_name, mode='wt', encoding="utf-8")
				file.write(content)
				file.close()
				sys.stdout.write(f"Data saved in file '{file_name}'.\n\n")
			except (OSError, IOError, UnicodeError) as error_msg:
				sys.stderr.write(f"[STDERR] Error opening file {file_name}: {error_msg}\n")
				sys.stderr.write(f"Data not saved.\n\n")


if __name__ == "__main__":
	if len(sys.argv) == 2:
		sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
		new_content = encode_str(get_file_content(sys.argv[1]))
		save_content(new_content)
	pass
