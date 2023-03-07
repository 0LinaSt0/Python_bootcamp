import pytest
import sys
from conftest import FALSE_ERROR, REACTION_DETECTOR_ERROR
sys.path.insert(1, "../../ex00")
from ReactionsDetector import ReactionsDetector


"""
**TESTS FOR REACTIONS_DETECTOR MODULE**

	``Finctions``

	check_is_human()
		Check is_human

"""


def check_is_human(obj, expected_result, err):
	try:
		ret = obj.is_human()
		assert ret == expected_result
	except ReactionsDetector.ReactionDetectorException as e:
		assert e.args[0] == err


class TestReactionsDetector:
	"""TestReactionsDetector class is used for testing ReactionsDetector

		``Methods``

		test_is_human_valid_replicant()
			Checking is_human on valid replicant case

		test_is_human_valid_human()
			Checking is_human on valid human case

		test_is_human_invalid()
			Checking is_human on invalid human case
	"""
	
	def test_is_human_valid_replicant(self, reactions_detector_valid_replicant_obj):
		check_is_human(
			reactions_detector_valid_replicant_obj, 
			False, 
			FALSE_ERROR
		)

	
	def test_is_human_valid_human(self, reactions_detector_valid_human_obj):
		check_is_human(
			reactions_detector_valid_human_obj, 
			True, 
			FALSE_ERROR
		)

	
	def test_is_human_invalid(self, reactions_detector_invalid_obj):
		check_is_human(
			reactions_detector_invalid_obj, 
			False, 
			REACTION_DETECTOR_ERROR
		)