import pytest
import sys
from conftest import FALSE_ERROR, REACTION_DETECTOR_ERROR
sys.path.insert(1, "../../ex00")
from ReactionsDetector import ReactionsDetector


def check_is_human(obj, expected_result, err):
	try:
		ret = obj.is_human()
		assert ret == expected_result
	except ReactionsDetector.ReactionDetectorException as e:
		assert e.args[0] == err


class TestReactionsDetector:
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