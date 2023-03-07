import pytest
import sys
import mock
import builtins
from conftest import (
	MockedX,
	INCORRECTLY,
	INPUT_FLAG,
	FALSE_ERROR,
	INVALID_INPUT_ERROR,
	INVALID_RANGE_ERROR
)
sys.path.insert(1, "../../ex00")
from Reaction import Reaction, Reactions


"""
**TESTS FOR INTERVIEWER MODULE**

	``Finctions``

	check_input()
		Check input

	check_grade()
		Check grade

	is_incorrect()
		Check on correct

"""


def check_input(reactions, argum, expected_result, err):
	try:
		for reaction in reactions:
			with mock.patch.object(builtins, INPUT_FLAG, lambda _: argum):
				reaction.read_input()
			assert reaction.grade == expected_result
	except Reaction.ReactionException as e:
		assert e.args[0] == err


def check_grade(reactions, grade, expected_result, err):
	try:
		for reaction in reactions:
			reaction.grade = grade
			reaction.check_grade()
			assert reaction.is_valid == expected_result
	except Reaction.ReactionException as e:
		assert e.args[0] == err


def is_incorrect(reaction, capsys, err):
	reaction.grade_reaction()
	out = capsys.readouterr()
	assert out.out == err


class TestReactions:
	"""TestReactions class is used for testing reactions

		``Methods``

		test_read_invalid_int_input()
			Checking read_input on invalid int

		test_read_valid_int_input()
			Checking read_input on valid int

		test_check_invalid_grade()
			Checking grade on invalid case

		test_check_valid_grade()
			Checking grade on valid case

		test_grade_reaction()
			Checking grade_reaction
	"""

	@pytest.fixture(autouse=True)
	def _reactions(self, respiration_obj, heartRate_obj,
					blushingLevel_obj, pupillaryDilation_obj):
		self.reactions1 = [
			respiration_obj, 
			heartRate_obj, 
			blushingLevel_obj, 
			pupillaryDilation_obj
		]

		self.reactions2 = [
			blushingLevel_obj, 
			pupillaryDilation_obj
		]

		self.reactions3 = [
			respiration_obj, 
			heartRate_obj
		]


	def test_read_invalid_int_input(self):
		check_input(self.reactions1, "asef", False, INVALID_INPUT_ERROR)
		check_input(self.reactions1, "-1c5d", False, INVALID_INPUT_ERROR)
		check_input(self.reactions1, "6cde8", False, INVALID_INPUT_ERROR)
		check_input(self.reactions1, "", False, INVALID_INPUT_ERROR)
		check_input(self.reactions1, "\n\t", False, INVALID_INPUT_ERROR)


	def test_read_valid_int_input(self):
		check_input(self.reactions1, 456, 456, FALSE_ERROR)
		check_input(self.reactions1, 45, 45, FALSE_ERROR)
		check_input(self.reactions1, 1, 1, FALSE_ERROR)
		check_input(self.reactions1, 6, 6, FALSE_ERROR)


	def test_check_invalid_grade(self):
		check_grade(self.reactions2, 10, False, INVALID_RANGE_ERROR)
		check_grade(self.reactions2, 0, False, INVALID_RANGE_ERROR)
		check_grade(self.reactions2, 645, False, INVALID_RANGE_ERROR)
		check_grade(self.reactions1, -132, False, INVALID_RANGE_ERROR)
		check_grade(self.reactions1, -1, False, INVALID_RANGE_ERROR)


	def test_check_valid_grade(self):
		check_grade(self.reactions1, 2, True, FALSE_ERROR)
		check_grade(self.reactions1, 3, True, FALSE_ERROR)
		check_grade(self.reactions1, 5, True, FALSE_ERROR)
		check_grade(self.reactions3, 456, True, FALSE_ERROR)
		check_grade(self.reactions3, 1, True, FALSE_ERROR)
		check_grade(self.reactions3, 12, True, FALSE_ERROR)


	@mock.patch("Reaction.Reaction.read_input", MockedX.change_read_input)
	@mock.patch("Reaction.Reaction.check_grade", MockedX.change_check_grade)
	def test_grade_reaction(self, capsys):
		is_incorrect(self.reactions1[0], capsys, INCORRECTLY)
		is_incorrect(self.reactions1[1], capsys, INCORRECTLY)
		is_incorrect(self.reactions1[2], capsys, INCORRECTLY)
		is_incorrect(self.reactions1[3], capsys, INCORRECTLY)


class TestReactionsCounter:
	"""TestReactions class is used for testing reactions

		``Methods``

		test_update_reaction()
			Checking update_reaction
	"""

	def test_update_reaction(self, reactions_counter_obj):
		reactions_counter_obj.update_reaction(
			Reactions.RESPIRATION, 3
		)
		reactions_counter_obj.update_reaction(
			Reactions.HEART_RATE, 3
		)
		reactions_counter_obj.update_reaction(
			Reactions.BLUSHING_LEVEL, 3
		)
		reactions_counter_obj.update_reaction(
			Reactions.PUPILLARY_DILATION, 3
		)
		for value in reactions_counter_obj.reactions.values():
			assert value == 3

