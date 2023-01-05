import pytest
import sys
import mock
from conftest import (
	MockedX,
	EXAMPLE_KEY,
	QUESTION_ERROR,
	REACTION_DETECTOR_ERROR
)
sys.path.insert(1, "../../ex00")
from Reaction import Reactions, ReactionsCounter
from Question import Question


HUMAN_STR = "\n\t~~~~~~~ Verdict ~~~~~~~\nYOU'R A HUMAN. YOU CAN BE FREE\n\n"
REPLICANT_STR = "\n\t~~~~~~~ Verdict ~~~~~~~\n!DANGER! REPLICANT WAS DETECTED\n\n"

"""
**TESTS FOR INTERVIEWER MODULE**

	``Finctions``

	check_verdict()
		Check verdict

"""


def check_verdict(capsys, obj, reaction, expected_result):
	obj.grades_reactions = reaction
	obj.verdict()
	out = capsys.readouterr()
	assert out.out == expected_result


class TestInterviewer:
	"""TestInterviewer class is used for testing interviewer

		``Methods``

		test_interview_process()
			Checking interview_process

		test_verdict()
			Checking verdict

		test_ask_question()
			Checking ask_question

		test_grade_answer_reaction()
			Checking grade_answer_reaction
	"""

	@pytest.fixture(autouse=True)
	def _reactions_counters(self):
		self.r_counter_human = ReactionsCounter()
		self.r_counter_replicant = ReactionsCounter()

		self.r_counter_human.reactions[Reactions.RESPIRATION] = 120
		self.r_counter_human.reactions[Reactions.HEART_RATE] = 900
		self.r_counter_human.reactions[Reactions.BLUSHING_LEVEL] = 60
		self.r_counter_human.reactions[Reactions.PUPILLARY_DILATION] = 45

		self.r_counter_replicant.reactions[Reactions.RESPIRATION] = 180
		self.r_counter_replicant.reactions[Reactions.HEART_RATE] = 200
		self.r_counter_replicant.reactions[Reactions.BLUSHING_LEVEL] = 20
		self.r_counter_replicant.reactions[Reactions.PUPILLARY_DILATION] = 30


	@mock.patch("Interviewer.Interviewer.ask_question", MockedX.change_ask_question)
	@mock.patch("Interviewer.Interviewer.grade_answer_reaction", MockedX.change_grade_answer_reaction)
	def test_interview_process(self, interviewer_obj):
		try:
			interviewer_obj.interview_process()
		except:
			pass


	def test_verdict(self, capsys, interviewer_obj):
		interviewer_obj.questions_count = 10
		check_verdict(capsys, interviewer_obj, 
						self.r_counter_human, HUMAN_STR)
		check_verdict(capsys, interviewer_obj,
						self.r_counter_replicant, REPLICANT_STR)
		interviewer_obj.questions_count = 0
		check_verdict(capsys, interviewer_obj, self.r_counter_replicant, 
						REACTION_DETECTOR_ERROR + '\n')


	@mock.patch("Question.Question.print_question", MockedX.change_print_question)
	@mock.patch("Question.Question.ask_answer", MockedX.change_ask_answer)
	@mock.patch("Answer.AnswersKeeper.save_answer", MockedX.change_save_answer)
	def test_ask_question(self, interviewer_obj):
		interviewer_obj.questions_count = 10
		try:
			interviewer_obj.ask_question(EXAMPLE_KEY)
		except Question.QuestionException as e:
			assert e.args[0] == QUESTION_ERROR


	@mock.patch("Reaction.Reaction.grade_reaction", MockedX.change_grade_reaction)
	@mock.patch("Reaction.ReactionsCounter.update_reaction", MockedX.change_update_reaction)
	def test_grade_answer_reaction(self, capsys, interviewer_obj):
		interviewer_obj.grade_answer_reaction()
		out = capsys.readouterr()
		assert out.out == "I SEE. YOUR ...\n"


