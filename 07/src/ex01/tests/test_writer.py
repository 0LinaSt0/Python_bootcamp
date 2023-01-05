import pytest
import sys
from json import load
from conftest import (
	PathsAnswers,
	WRITER_ERROR,
	FALSE_ERROR
)
sys.path.insert(1, "../../ex00")
from Writer import Writer


def check_write_to_file(obj, path, data, err):
	try:
		obj.write_to_file(path, data)
		with open(path, "r") as openfile:
			assert load(openfile) == data
	except Writer.WriterException as e:
		assert e.args[0] == err


class TestWriter:
	def test_write_to_file(self, writer_obj, answers_dict_obj):
		check_write_to_file(
			writer_obj,
			PathsAnswers.VALID.value,
			answers_dict_obj,
			FALSE_ERROR
		)

		check_write_to_file(
			writer_obj,
			PathsAnswers.INVALID_WITHOUT_PERMIT.value,
			answers_dict_obj,
			WRITER_ERROR(PathsAnswers.INVALID_WITHOUT_PERMIT.value)
		)

