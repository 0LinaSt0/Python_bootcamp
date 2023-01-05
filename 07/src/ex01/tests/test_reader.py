import pytest
import sys
from conftest import (
	PathsQuestions,
	READER_ERROR,
	FALSE_ERROR
) 
sys.path.insert(1, "../../ex00")
from Reader import Reader


"""
**TESTS FOR READER MODULE**

	``Finctions``

	check_read_file()
		Check read_file

"""



def check_read_file(obj, path, expected_result, err):
	try:
		q = obj.read_file(path)
		assert q == expected_result
	except Reader.ReaderException as e:
		assert e.args[0] == err


class TestReader:
	"""TestReader class is used for testing reader

		``Methods``

		test_read_file()
			Checking read_file
	"""

	def test_read_file(self, reader_obj, questions_dict_obj):
		check_read_file(
			reader_obj, 
			PathsQuestions.VALID.value, 
			questions_dict_obj, 
			FALSE_ERROR
		)

		check_read_file(
			reader_obj,
			PathsQuestions.INVALID_EMPTY.value, 
			False, 
			READER_ERROR(PathsQuestions.INVALID_EMPTY.value)
		)

		check_read_file(
			reader_obj,
			PathsQuestions.INVALID_WITHOUT_PERMIT.value,
			False,
			READER_ERROR(PathsQuestions.INVALID_WITHOUT_PERMIT.value)
		)