"""
Command for using this functions with all files:
	$ pytest -k divisible -v
"""

import pytest, sys
sys.path.insert(1, "../../ex00")
from answers import Answers
from questions import Questions
from reactions import Reactions


"""
[2, 3, 1, 5, "ddd", 896, 0, 2, 1, 1, 2, 1, 1, 1], # replicant scenario ([3;6] invalid)
[3, 3, 1, 0, "ds", -8, 12, 2, 2, 2, 2, 1, 3, 3] # human scenario ([3;6] invalid)
"""

@pytest.fixture
def send_answers():
	return [2, 3, 1, 5, "ddd", 896, 0, 2, 1, 1, 2, 1, 1, 1]


@pytest.fixture
def send_degree():
	return [
		[11, 5, 2, 4, 66, 50, 1, 2, 7, 100, 3, 4, 15, 70, 4, 4,
			17, 5, 2, 5, 33, 12, 3, 7, 15, 60, 1, 2, 2, 120, 2, 2,
			9, 30, 3, 5, 13, 66, 3, 3
		], # replicant scenario
		[11, 77, 5, 8, 15, 90, 4, 6, 107, 100, 6, 7, 15, 70, 3, 4,
			17, 50, 3, 5, 16, 74, 5, 7, 15, 60, 3, 8, 13, 110, 5, 4,
			11, 99, 5, 5, 13, 66, 3, 5
		] # human scenario
	]


@pytest.fixture
def create_questions():
	return Questions()


@pytest.fixture
def create_answers():
	return Answers()


@pytest.fixture
def create_reactions():
	return Reactions()
