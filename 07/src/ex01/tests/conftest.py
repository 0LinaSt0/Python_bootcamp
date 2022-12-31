"""
Command for using this functions with all files:
	$ pytest -k divisible -v
"""

import pytest, sys
sys.path.insert(1, "../ex00")
from answers import Answers
from questions import Questions
from reactions import Reactions


@pytest.fixture
def questions_valid_obj():
	return Questions("srcs_questions/valid.json")


@pytest.fixture
def questions_invalid_obj():
	return Questions("srcs_questions/invalid.json")


@pytest.fixture
def questions_withoutPerform_obj():
	return Questions("srcs_questions/without_permission.json")


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
