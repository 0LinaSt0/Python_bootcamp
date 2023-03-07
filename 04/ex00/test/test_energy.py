"""
Run tests (inside test directory):
	~$ pythest -v
"""


import pytest, sys
sys.path.insert(1, "../")
from energy import *


def test_subject_first(subject_first_result):
	returned = [elem for elem in fix_wiring(['cable1', 'cable2', 'cable3', 'cable4'],
				['socket1', 'socket2', 'socket3', 'socket4'],
				['plug1', 'plug2', 'plug3'])]
	assert returned == subject_first_result


def test_subject_second(subject_second_result):
	returned = [elem for elem in fix_wiring(['cable2', 'cable1', False],
				[1, 'socket1', 'socket2', 'socket3', 'socket4'],
				['plugZ', None, 'plugY', 'plugX'])]
	assert returned == subject_second_result


def test_empty_plugs(empty_plugs_result):
	returned = [elem for elem in fix_wiring(['cable2', 'cable1', False],
				[1, 'socket1', 'socket2', 'socket3', 'socket4'], [])]
	assert returned == empty_plugs_result


def test_empty_cables(empty_cables_result):
	returned = [elem for elem in fix_wiring([],
				[1, 'socket1', 'socket2', 'socket3', 'socket4'],
				['plugZ', None, 'plugY', 'plugX'])]
	assert returned == empty_cables_result


def test_one_socket(one_socket_result):
	returned = [elem for elem in fix_wiring(['cable2', 'cable1', False],
				[1, 'socket1', ], ['papa', 'pluww', 'PLU4'])]
	assert returned == one_socket_result
