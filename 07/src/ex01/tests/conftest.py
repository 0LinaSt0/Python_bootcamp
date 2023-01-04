"""
Command for using this functions with all files:
	$ pytest -k divisible -v
"""

import pytest
import sys
from enum import Enum
from json import load
sys.path.insert(1, "../../ex00")
from Interviewer import Interviewer
from Question import Question
from Answer import Answer, AswersKeeper
from ReactionsDetector import ReactionsDetector
from Reaction import (
	Reactions,
	Respiration,
	HeartRate,
	BlushingLevel,
	PupillaryDilation,
	ReactionsCounter
)

INCORRECTLY = "\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m\n"
INVALID_INPUT_ERROR = "\nError: invalid input\n"
INVALID_RANGE_ERROR = "\nError: out of range\n"
REACTION_DETECTOR_ERROR = "\nError: something wrong: check arguments in ReactionsDetector.is_reaction_norm\n"
FALSE_ERROR = "WRONG"
INPUT_FLAG = "input"


class Paths(Enum):
	VALID = "srcs_questions/valid.json",
	INVALID_EMPTY = "srcs_questions/invalid_empty.json",
	INVALID_ANSWERS = "srcs_questions/invalid_answers.json",
	INVALID_WITHOUT_PERMIT = "srcs_questions/without_permission.json"


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
	return AswersKeeper()


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
	with open(Paths.VALID.value[0], "r") as openfile:
		return load(openfile)


@pytest.fixture
def interviewer_obj():
	return Interviewer(questions_dict())