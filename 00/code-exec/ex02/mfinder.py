"""
The script finds M-pattern (imaging with '*') in input file
and returns:
	- "True": M-pattern exists
	- "False": M-pattern doesn't exist
	- "Error": gave 2d map is not VERTICALxHORIZONTAL

Run the script:
	~$ cat m.txt | python mfinder.py
"""

import sys
import enum

HORIZONTAL = 5
VERTICAL = 3
class statuses(enum.Enum):
	ERROR = "Error"
	TRUE = "True"
	FALSE = "False"


def invalid_exit(status):
	print(status)
	exit()


def create_map():
	invalid_flag = False
	line_counter = 0
	input_map = []
	for line in sys.stdin:
		if len(line.rstrip()) != HORIZONTAL or line_counter >= VERTICAL:
			invalid_flag = True
			break
		input_map.append(line.rstrip())
		line_counter += 1
	if invalid_flag is True or line_counter != VERTICAL:
		invalid_exit(statuses.ERROR.value)
	return input_map


def check_value_for_validity(line, vertical_number):
	last_elem = HORIZONTAL - 1
	for i in range(HORIZONTAL):
		if (
			i == 0 or i == last_elem
			or (vertical_number <= (last_elem // 2)
			and (i == vertical_number
			or (i == last_elem - vertical_number)))
		):
			if (line[i] != '*'):
				invalid_exit(statuses.FALSE.value)
		else:
			if (line[i] == '*'):
				invalid_exit(statuses.FALSE.value)


if "__main__" == __name__:
	input_map = create_map()

	for line_index in range(VERTICAL):
		check_value_for_validity(input_map[line_index], line_index)

	print(statuses.TRUE.value)
