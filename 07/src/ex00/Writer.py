from json import dumps

class Writer:
	def __init__(self, path, data):
		self.path = path
		self.data = data


	class WriterException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def write_to_file(self):
		try:
			json_object = dumps(self.data, indent=4)
			with open(self.path, "w") as outfile:
				outfile.write(json_object)
		except:
			raise Writer.WriterException(
				"\nError: couldn't write data in \"{}\"\n".format(self.path)
			)