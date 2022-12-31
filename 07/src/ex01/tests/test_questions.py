import pytest


def test_valid_questions_file(capfd, questions_valid_obj):
	out, err = capfd.readouterr()
	assert out == "Success creating\n"


def test_invalid_questions_file(capfd, questions_invalid_obj):
	out, err = capfd.readouterr()
	assert out == "File \"srcs_questions/invalid.json\" didn't exec\n"

