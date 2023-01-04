import pytest
import sys
import mock
from conftest import (
	FALSE_ERROR,
	REACTION_DETECTOR_ERROR
)
sys.path.insert(1, "../../ex00")
from ReactionsDetector import ReactionsDetector
from Reaction import Reactions


HUMAN_STR = "\n\t~~~~~~~ Verdict ~~~~~~~\nYOU'R A HUMAN. YOU CAN BE FREE\n"
REPLICANT_STR = "\n\t~~~~~~~ Verdict ~~~~~~~\n!DANGER! REPLICANT WAS DETECTED\n"


def check_verdict(capsys, obj, reaction, expected_result, err):
	try:
		obj.grades_reactions = reaction
		print(obj.grades_reactions.reactions)
		obj.verdict()
		out = capsys.readouterr()
		assert out.out == expected_result
	except ReactionsDetector.ReactionDetectorException as e:
		assert e.args[0] == err


class MockedX:
	def change_ask_question(self):
		pass


	def change_grade_answer_reaction(self):
		pass


class TestInterviewer:
	@pytest.fixture(autouse=True)
	def _reactions_counters(self, reactions_counter_obj):
		self.r_counter_human = reactions_counter_obj
		self.r_counter_replicant = reactions_counter_obj

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
		interviewer_obj.interview_process()


	def test_verdict(self, interviewer_obj):
		pass


	def test_ask_question(self):
		pass


	def test_grade_answer_reaction(self):
		pass


