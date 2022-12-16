"""
Run tests (inside test directory):
	~$ pytest -v
"""

import pytest, sys
sys.path.insert(1, "../")
from key import Key


def test_key():
	key = Key()
	assert len(key) == 1337
	assert key[404] == 3
	assert key > 9000
	assert key.passphrase == "zax2rulez"
	assert str(key) == "GeneralTsoKeycard"
