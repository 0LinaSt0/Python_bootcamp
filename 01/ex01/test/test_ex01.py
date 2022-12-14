"""
Run tests (inside test directory):
	~$ pytest -v
"""

import pytest, sys
sys.path.insert(1, "../")
from ex01 import *


def test_split_booty(some_purses_with_gold, some_purses_without_gold,
						some_purses_with_one_gold, some_purses_with_two_gold,
						one_purse_with_gold):
	assert split_booty(*some_purses_with_gold) == ({'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1})
	assert split_booty(*some_purses_without_gold) == ({'gold_ingots': 0}, {'gold_ingots': 0}, {'gold_ingots': 0})
	assert split_booty(*some_purses_with_one_gold) == ({'gold_ingots': 1}, {'gold_ingots': 0}, {'gold_ingots': 0})
	assert split_booty(*some_purses_with_two_gold) == ({'gold_ingots': 1}, {'gold_ingots': 1}, {'gold_ingots': 0})
	assert split_booty(one_purse_with_gold) == ({'gold_ingots': 189}, {'gold_ingots': 188}, {'gold_ingots': 188})
