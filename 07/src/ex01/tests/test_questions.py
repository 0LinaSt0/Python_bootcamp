import pytest
import sys
from json import load
sys.path.insert(1, "../ex00")
from questions import Reader
from customException import customException


def test_valid_questions_file(capsys):
	path = "srcs_questions/valid.json"
	Reader(path)
	out = capsys.readouterr()
	assert out.out == "Success creating\n"


def test_invalid_questions_file():
	path = "srcs_questions/invalid.json"
	try:
		Reader(path)
	except customException as e:
		assert e.args[0] == f"\nError: file \"{path}\" cannot be executed\n"


def test_withoutPerform_questions_file():
	path = "srcs_questions/without_permission.json"
	try:
		Reader(path)
	except customException as e:
		assert e.args[0] == f"\nError: file \"{path}\" cannot be executed\n"


def questions_generator(path):
	with open(path, "r") as openfile:
		questions = load(openfile)
		return (question for question in questions)


def test_out_questions():
	path = "srcs_questions/valid.json"
	default_questions = questions_generator(path)
	returned_questions = Reader(path).out_questions()
	for q1, q2 in zip(default_questions, returned_questions):
		assert q1 == q2