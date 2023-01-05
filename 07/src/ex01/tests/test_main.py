import pytest
import sys
import mock
from conftest import (
	MockedX,
	PathsQuestions,
	READER_ERROR,
	WRITER_ERROR
)
sys.path.insert(1, "../../ex00")
from Reader import Reader
from Writer import Writer
from main import (
	take_questions,
	write_answers,
	programm_process
)


def change_take_questions(p):
	pass


def change_write_answers(a, b):
	pass


@mock.patch("Reader.Reader.read_file", MockedX.change_read_file)
def test_take_questions_valid(questions_dict_obj):
	assert take_questions(PathsQuestions.VALID.value) == questions_dict_obj


@mock.patch("Reader.Reader.read_file", MockedX.change_read_file_except)
def test_take_questions_invalid(capsys):
	try:
		path = PathsQuestions.INVALID_EMPTY.value
		with pytest.raises(SystemExit) as system_exit:
			take_questions(path)
	except Reader.ReaderException:
		assert system_exit.value.code == READER_ERROR(path)


@mock.patch("Writer.Writer.write_to_file", MockedX.change_write_to_file)
def test_write_answers(capsys, answers_dict_obj):
	try:
		path = PathsQuestions.VALID.value
		write_answers(answers_dict_obj, path)
	except Writer.WriterException:
		out = capsys.readouterr()
		assert out.out == WRITER_ERROR(path)


@mock.patch("Interviewer.Interviewer.interview_process", MockedX.change_interview_process)
@mock.patch("Interviewer.Interviewer.verdict", MockedX.change_verdict)
@mock.patch("main.take_questions", change_take_questions)
@mock.patch("main.write_answers", change_write_answers)
def test_programm_process():
	programm_process()