import pytest
import sys
import mock
import builtins
from conftest import (
	MockedX, 
	EXAMPLE_KEY,
	INCORRECTLY,
	INPUT_FLAG,
	FALSE_ERROR,
	INVALID_INPUT_ERROR,
	INVALID_RANGE_ERROR
)
sys.path.insert(1, "../../ex00")
from Answer import Answer


"""
**TESTS FOR ANSWER MODULE**

	``Finctions``
		
	check_input()
		Check inputs
		
	check_answer()
		Check answers

"""



def check_input(obj, argum, expected_result, err):
	try:
		with mock.patch.object(builtins, INPUT_FLAG, lambda _: argum):
			obj.read_input()
		assert obj.num_answer == expected_result
	except Answer.AnswerException as e:
		assert e.args[0] == err


def check_answer(obj, num_argum, expected_result, err):
	try:
		obj.num_answer = num_argum
		obj.check_answer()
		assert obj.is_valid == expected_result
	except Answer.AnswerException as e:
		assert e.args[0] == err


class TestAnswer:
	"""TestAnswer class is used for testing answers

		``Methods``

		test_read_invalid_int_input()
			Checking invalid input

		test_valid_int_input()
			Checking valid int input

		test_check_invalid_answer()
			Checking invalid answer

		test_check_valid_answer()
			Checking valid answer

		test_take_answer()
			Checking tacke answer
	"""

	def test_read_invalid_int_input(self, answer_obj):
		check_input(answer_obj, "dvzdfgv", False, INVALID_INPUT_ERROR)
		check_input(answer_obj, "-5f6", False, INVALID_INPUT_ERROR)
		check_input(answer_obj, "6d8", False, INVALID_INPUT_ERROR)
		check_input(answer_obj, "", False, INVALID_INPUT_ERROR)
		check_input(answer_obj, "\n", False, INVALID_INPUT_ERROR)


	def test_valid_int_input(self, answer_obj):
		check_input(answer_obj, 1, 1, FALSE_ERROR)
		check_input(answer_obj, 2, 2, FALSE_ERROR)
		check_input(answer_obj, 3, 3, FALSE_ERROR)


	def test_check_invalid_answer(self, answer_obj):
		check_answer(answer_obj, 0, False, INVALID_RANGE_ERROR)
		check_answer(answer_obj, -456, False, INVALID_RANGE_ERROR)
		check_answer(answer_obj, -4, False, INVALID_RANGE_ERROR)
		check_answer(answer_obj, 6, False, INVALID_RANGE_ERROR)


	def test_check_valid_answer(self, answer_obj):
		check_answer(answer_obj, 1, True, FALSE_ERROR)
		check_answer(answer_obj, 3, True, FALSE_ERROR)
		check_answer(answer_obj, 2, True, FALSE_ERROR)


	@mock.patch("Answer.Answer.read_input", MockedX.change_read_input)
	@mock.patch("Answer.Answer.check_answer", MockedX.change_check_answer)
	def test_take_answer(self, capsys, answer_obj):
		answer_obj.take_answer()
		out = capsys.readouterr()
		assert out.out == INCORRECTLY


class TestAnswerKeeper:
	"""TestAnswerKeeper class is used for testing answers keeper

	``Methods``

	test_save_answer()
		Checking save answer
	"""

	def test_save_answer(self, answer_keeper_obj, answer_obj):
		answer_keeper_obj.save_answer(answer_obj.question, 2)
		for key, value in answer_keeper_obj.answers.items():
			assert key == EXAMPLE_KEY
			assert value == 2