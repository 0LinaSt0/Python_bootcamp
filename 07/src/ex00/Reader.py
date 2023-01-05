from json import load


class Reader:
	"""Reader class is used for creating dict from reading file

	``Attributes``

	:param class ReaderException: custom exception for Reader class


	``Methods``

	read_file()
		Reads file and generate dict
	
	"""

	class ReaderException(Exception):
		"""Custom exception for Reader inherited from Exception

		``Attributes``
		
		:param string message: exception message

		"""
		
		def __init__(self, message) -> None:
			super().__init__(message)


	def read_file(self, path):
		"""Reads file and generate dict: if it possible

		:param string path: path to readed file
		:raise Reader.ReaderException: if file cannot be executed
		:return: the dict
		:rtype: dict
		"""

		try:
			with open(path, "r") as openfile:
				log = load(openfile)
				return log
		except:
			raise Reader.ReaderException(
				"\nError: file \"{}\" cannot be executed\n".format(path)
			)
