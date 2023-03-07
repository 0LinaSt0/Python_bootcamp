"""
The script finds and returns lines which:
	- are 32 characters long
	- start with exactly 5 zeroes

Run the script:
	~$ cat data_hashes_10lines.txt | python blocks.py 10
"""

import sys

if "__main__" == __name__:
	lines_count = int(sys.argv[1])
	zero_count = 0

	for line, _ in zip(sys.stdin, range(lines_count)):
		while line[zero_count] == '0':
			zero_count += 1
		# rstrip method removes a trailing newline (\n)
		if (zero_count == 5 and len(line.rstrip()) == 32):
			print(line.rstrip())
		zero_count = 0
