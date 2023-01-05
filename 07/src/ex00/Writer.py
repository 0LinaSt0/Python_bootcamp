from json import dumps

class Writer:
	"""Writer class is used for creating file with coming data

	``Attributes``

	:param class WriterException: custom exception for Writer class


	``Methods``

	write_to_file()
		Write coming data to file
	
	"""
	class WriterException(Exception):
		"""Custom exception for Writer inherited from Exception

		``Attributes``
		
		:param string message: exception message

		"""
		def __init__(self, message) -> None:
			super().__init__(message)


	def write_to_file(self, path, data):
		"""Write coming data to file: if it possible

		:param string path: path for writing file
		:param string data: writing information
		:raise Writer.WriterException: if couldn't write data to file
		"""
		try:
			json_object = dumps(data, indent=4)
			with open(path, "w") as outfile:
				outfile.write(json_object)
		except:
			raise Writer.WriterException(
				"\nError: couldn't write data in \"{}\"\n".format(path)
			)