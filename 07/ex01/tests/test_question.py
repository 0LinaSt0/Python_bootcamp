import pytest
import mock
import sys
from conftest import MockedX, QUESTION_ERROR
sys.path.insert(1, "../../ex00")
from Question import Question


VALID_STRING = "\n1. Your little boy shows you his butterfly collection, plus the killing jar. What do you say?\n\t1) Oh, lovely!\n\t2) That's nice, but why don't you keep the killing jar for yourself?\n\t3) Nothing. I take my boy to the doctor\n"

"""
**TESTS FOR QUESTION MODULE**
"""


class TestQuestion:
	"""TestAnswer class is used for testing answers

		``Methods``

		test_print_valid_question()
			Checking print_question on valid case

		test_print_invalid_question()
			Checking print_question on invalid case

		test_check_ask_answer()
			Checking ask_answer
	"""

	def test_print_valid_question(self, capsys, question_valid_obj):
		question_valid_obj.print_question()
		out = capsys.readouterr()
		assert out.out == VALID_STRING


	def test_print_invalid_question(self, question_invalid_obj):
		try:
			question_invalid_obj.print_question()
		except Question.QuestionException as e:
			assert e.args[0] == QUESTION_ERROR


	@mock.patch("Answer.Answer.take_answer", MockedX.change_ask_answer)
	def test_check_ask_answer(self, question_valid_obj):
		question_valid_obj.ask_answer()



