"""
Run tests (inside test directory):
	~$ pytest -v
"""

import pytest, sys
sys.path.insert(1, "../")
from ex00 import *

def test_empty_func(purse_empty, purse_just_gold, purse_not_just_gold,
					purse_zero_gold, purse_without_gold):
	assert empty(purse_empty) == {}
	assert empty(purse_just_gold) == {}
	assert empty(purse_not_just_gold) == {}
	assert empty(purse_zero_gold) == {}
	assert empty(purse_without_gold) == {}


def test_addIngot_func(purse_empty, purse_just_gold, purse_not_just_gold,
					purse_zero_gold, purse_without_gold):
	assert add_ingot(purse_empty) == {"gold_ingots": 1}
	assert add_ingot(purse_just_gold) == {"gold_ingots": 4}
	assert add_ingot(purse_not_just_gold) == {"gold_ingots": 57, "rocks": 5, "buttons": 4}
	assert add_ingot(purse_zero_gold) == {"gold_ingots": 1}
	assert add_ingot(purse_without_gold) == {"rocks": 2, "buttons": 0, "paperclips": 10, "gold_ingots": 1}


def test_getIngot_func(purse_empty, purse_just_gold, purse_not_just_gold,
					purse_zero_gold, purse_without_gold):
	assert get_ingot(purse_empty) == {}
	assert get_ingot(purse_just_gold) == {"gold_ingots": 2}
	assert get_ingot(purse_not_just_gold) == {"gold_ingots": 55, "rocks": 5, "buttons": 4}
	assert get_ingot(purse_zero_gold) == {"gold_ingots": 0}
	assert get_ingot(purse_without_gold) == {"rocks": 2, "buttons": 0, "paperclips": 10}

