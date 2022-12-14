"""
Run tests (inside test directory):
	~$ pytest -v
"""

import pytest, sys
sys.path.insert(1, "../")
from ex02 import *


def test_wrapper_for_get(capsys):
	assert get_ingot({'gold_ingots': 10}) == {'gold_ingots': 9}
	stdout = capsys.readouterr() #for checking stdout
	assert stdout.out == "SQUEAK\n"


def test_wrapper_for_empty(capsys):
	assert empty({'gold_ingots': 2}) == {}
	stdout = capsys.readouterr() #for checking stdout
	assert stdout.out == "SQUEAK\n"


def test_wrapper_for_add(capsys):
	assert add_ingot({'gold_ingots': 4}) == {'gold_ingots': 5}
	stdout = capsys.readouterr() #for checking stdout
	assert stdout.out == "SQUEAK\n"
