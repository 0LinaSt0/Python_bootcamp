import pytest
from mock import patch
from teesrclass import Teest

def t():
	return Teest().inside_teest()


class Test:

	@patch("test.Teest.inside_teest")
	def tester(self, mock_inside_teest):
		expected_value = 2
		mock_inside_teest.return_value = expected_value
		
		ret = t()
		
		print(ret)

		assert ret == 2