

class customException(Exception):
	def __init__(self, message="WRONG") -> None:
		self.message = message
		super().__init__(self.message)
