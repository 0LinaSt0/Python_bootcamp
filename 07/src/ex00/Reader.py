from json import load


class Reader:
	def __init__(self, path):
		self.readed_dict = self.read_file(path)


	class ReaderException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def read_file(self, path):
		try:
			with open(path, "r") as openfile:
				log = load(openfile)
				return log
		except:
			raise Reader.ReaderException(
				"\nError: file \"{}\" cannot be executed\n".format(path)
			)
