"""
Command for using this functions with all files:
	$ pytest -k divisible -v
"""

import pytest, sys
sys.path.insert(1, "../ex00")
from answers import Answers
from reactions import Reactions


INCORRECTLY = "!INCORRECTLY!\n"
CORRECTLY = "CORRECTLY\n"
INPUT_FLAG = "input"

@pytest.fixture
def answers_obj():
	return Answers()


@pytest.fixture
def reactions_obj():
	return Reactions()


@pytest.fixture
def answers_replicant_scenario():
	return {
		1: 1,
		2: 2,
		3: 1,
		4: 2,
		5: 1,
		6: 2,
		7: 1,
		8: 2,
		9: 3,
		10: 1
	}


@pytest.fixture
def answer_human_scenario():
	return {
		1: 3,
		2: 2,
		3: 3,
		4: 2,
		5: 3,
		6: 2,
		7: 3,
		8: 2,
		9: 1,
		10: 3
	}


"""
if __name__ == "__main__":
	obj = Questions("valid.json")
	obj = Questions("srcs_questions/without_perform.json")
	for elem in obj.out_questions():
		print(elem)
"""
