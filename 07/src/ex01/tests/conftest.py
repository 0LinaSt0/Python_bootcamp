"""
Command for using this functions with all files:
	$ pytest -k divisible -v
"""

import pytest
import sys
from enum import Enum
from json import load
sys.path.insert(1, "../../ex00")
from Reader import Reader
from Writer import Writer
from Interviewer import Interviewer
from Question import Question
from Answer import Answer, AnswersKeeper
from ReactionsDetector import ReactionsDetector
from Reaction import (
	Reactions,
	Respiration,
	HeartRate,
	BlushingLevel,
	PupillaryDilation,
	ReactionsCounter
)

INVALID_INPUT_ERROR = "\nError: invalid input\n"
INVALID_RANGE_ERROR = "\nError: out of range\n"
REACTION_DETECTOR_ERROR = "\nError: something wrong: check arguments in ReactionsDetector.is_reaction_norm\n"
QUESTION_ERROR = "\nError: answer options are missing\n"
READER_ERROR = lambda p: "\nError: file \"{}\" cannot be executed\n".format(p)
WRITER_ERROR = lambda p: "\nError: couldn't write data in \"{}\"\n".format(p)
FALSE_ERROR = "WRONG"

INCORRECTLY = "\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m\n"
INPUT_FLAG = "input"
EXAMPLE_KEY = "You're watching television. Suddenly you spot a wasp crawling on your arm. How do you react?"


class PathsQuestions(Enum):
	VALID = "srcs_tests/valid.json"
	INVALID_EMPTY = "srcs_tests/invalid_empty.json"
	INVALID_WITHOUT_PERMIT = "srcs_tests/without_permission.json"


class PathsAnswers(Enum):
	VALID = "srcs_tests/valid_answers.json"
	INVALID_WITHOUT_PERMIT = "srcs_tests/without_permission_answers.json"


class MockedX:
	def change_read_file(self, a):
		return questions_dict()


	def change_interview_process(self):
		self.answers.answers = {
			"Someone gives you a calfskin wallet for your birthday. How do you react?": 3,
			"Your little boy shows you his butterfly collection, plus the killing jar. What do you say?": 3,
			"You're watching television. Suddenly you spot a wasp crawling on your arm. How do you react?": 3,
			"You're reading a magazine. You come across a full-page nude photo of a girl or guy. You show it to your husband/wife, who likes it so much, he/she hangs it on your bedroom wall. The girl/guy is lying on a bearskin rug.": 3,
			"While walking along in desert sand, you suddenly look down and see a tortoise crawling toward you. You reach down and flip it over onto its back. The tortoise lies there, its belly baking in the hot sun, beating its legs, trying to turn itself over, but it cannot do so without your help. You are not helping. Why?": 3,
			"Describe in single words only the good things that come to mind about your mother.": 3,
			"React to this: You become pregnant by a man who runs off with your best friend. You decide to get an abortion.": 3,
			"React to this: You're watching a stage play. A banquet is in progress. The guests are enjoying an appetizer of raw oysters. The entree consists of boiled dog stuffed with rice. The raw oysters are less acceptable to you than a dish of boiled dog.": 3,
			"The test is over. How many answers do you think were given by machines?": 3,
			"Thank you for participating! How did you like the test? (This question will not affect your result)": 3
		}


	def change_verdict(self):
		pass


	def change_read_file_except(self, path):
		raise Reader.ReaderException(READER_ERROR(path))


	def change_write_to_file(self, path, b):
		raise Writer.WriterException(WRITER_ERROR(path))
	
	
	def change_read_input(self):
		pass
	
	
	def change_check_answer(self):
		self.is_valid = True
		raise Answer.AnswerException("\nError: invalid input\n")

	
	def change_ask_answer(self):
		answer = Answer(
		"You're watching television. Suddenly you spot a wasp crawling on your arm. How do you react?",
		{
			"1": "I scream, then grab the closest object to me (which happens to be a can of sunscreen) and beat the hell out of it",
			"2": "I swat it away",
			"3": "I kill it"
		}
		)
		answer.num_answer = 1
		return answer


	def change_read_input(self):
		pass


	def change_check_grade(self):
		self.is_valid = True
		raise Reaction.ReactionException("\nError: out of range\n")

	
	def change_ask_question(self, a):
		pass


	def change_print_question(self):
		pass


	def change_grade_answer_reaction(self):
		raise Reaction.ReactionException("\nError: invalid input\n")

	
	def change_save_answer(self, a, b):
		raise Question.QuestionException("\nError: answer options are missing\n")
	
	
	def change_grade_reaction(self):
		self.grade = 1
	

	def change_update_reaction(self, a, b):
		pass



@pytest.fixture
def question_valid_obj():
	return Question(
		1, 
		"Your little boy shows you his butterfly collection, plus the killing jar. What do you say?",
		{
			"1": "Oh, lovely!",
			"2": "That's nice, but why don't you keep the killing jar for yourself?",
			"3": "Nothing. I take my boy to the doctor"
		}
	)


@pytest.fixture
def question_invalid_obj():
	return Question(
		2, 
		"Someone gives you a calfskin wallet for your birthday. How do you react?",
		{}
	)


@pytest.fixture
def answer_obj():
	return Answer(
		"You're watching television. Suddenly you spot a wasp crawling on your arm. How do you react?",
		{
			"1": "I scream, then grab the closest object to me (which happens to be a can of sunscreen) and beat the hell out of it",
			"2": "I swat it away",
			"3": "I kill it"
		}
	)


@pytest.fixture
def answer_keeper_obj():
	return AnswersKeeper()


@pytest.fixture
def respiration_obj():
	return Respiration()


@pytest.fixture
def heartRate_obj():
	return HeartRate()


@pytest.fixture
def blushingLevel_obj():
	return BlushingLevel()


@pytest.fixture
def pupillaryDilation_obj():
	return PupillaryDilation()


@pytest.fixture
def reactions_counter_obj():
	return ReactionsCounter()


@pytest.fixture
def reactions_detector_valid_replicant_obj():
	return ReactionsDetector(
		{
			Reactions.RESPIRATION: 180,
			Reactions.HEART_RATE: 200,
			Reactions.BLUSHING_LEVEL: 20,
			Reactions.PUPILLARY_DILATION: 30
		},
		10
	)


@pytest.fixture
def reactions_detector_valid_human_obj():
	return ReactionsDetector(
		{
			Reactions.RESPIRATION: 120,
			Reactions.HEART_RATE: 900,
			Reactions.BLUSHING_LEVEL: 60,
			Reactions.PUPILLARY_DILATION: 45
		},
		10
	)


@pytest.fixture
def reactions_detector_invalid_obj():
	return ReactionsDetector(
		{
			Reactions.RESPIRATION: 0,
			Reactions.HEART_RATE: 5,
			Reactions.BLUSHING_LEVEL: 74,
			Reactions.PUPILLARY_DILATION: 0
		},
		0
	)


def questions_dict():
	with open(PathsQuestions.VALID.value, "r") as openfile:
		return load(openfile)


@pytest.fixture
def questions_dict_obj():
	return (questions_dict())


@pytest.fixture
def answers_dict_obj():
	return {
		"Someone gives you a calfskin wallet for your birthday. How do you react?": 3,
		"Your little boy shows you his butterfly collection, plus the killing jar. What do you say?": 3,
		"You're watching television. Suddenly you spot a wasp crawling on your arm. How do you react?": 3,
		"You're reading a magazine. You come across a full-page nude photo of a girl or guy. You show it to your husband/wife, who likes it so much, he/she hangs it on your bedroom wall. The girl/guy is lying on a bearskin rug.": 3,
		"While walking along in desert sand, you suddenly look down and see a tortoise crawling toward you. You reach down and flip it over onto its back. The tortoise lies there, its belly baking in the hot sun, beating its legs, trying to turn itself over, but it cannot do so without your help. You are not helping. Why?": 3,
		"Describe in single words only the good things that come to mind about your mother.": 3,
		"React to this: You become pregnant by a man who runs off with your best friend. You decide to get an abortion.": 3,
		"React to this: You're watching a stage play. A banquet is in progress. The guests are enjoying an appetizer of raw oysters. The entree consists of boiled dog stuffed with rice. The raw oysters are less acceptable to you than a dish of boiled dog.": 3,
		"The test is over. How many answers do you think were given by machines?": 3,
		"Thank you for participating! How did you like the test? (This question will not affect your result)": 3
	}


@pytest.fixture
def interviewer_obj():
	return Interviewer(questions_dict())


@pytest.fixture
def reader_obj():
	return Reader()


@pytest.fixture
def writer_obj():
	return Writer()