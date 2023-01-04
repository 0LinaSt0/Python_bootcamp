"""
Answer evaluation:
	1 - it's definitely a replicant (1 score)
	2 - it's could be a human or a replicant (2 score)
	3 - it's definitely a human (3 score)

	scorses:
	a) [10; 20) - a replicant
	b) [20; 30] - a human
"""

class Answer:
	def __init__(self, question, answer_options: dict):
		self.question = question
		self.answer_options = answer_options
		self.is_valid = False
		self.num_answer: int


	class AnswerException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def take_answer(self):
		while not self.is_valid:
			try:
				self.read_input()
				self.check_answer()
			except:
				print("\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m")

	
	def read_input(self):
		try:
			self.num_answer = int(input("\nPLEASE, GIVE ME NUMBER OF ANSWER (INT): "))
		except:
			raise Answer.AnswerException("\nError: invalid input\n")


	def check_answer(self):
		if self.num_answer not in range(1, (len(self.answer_options) + 1)):
			raise Answer.AnswerException("\nError: out of range\n")
		self.is_valid = True




class AswersKeeper:
	def __init__(self):
		self.answers = {}

	
	def save_answer(self, question, answer):
		self.answers[question] = answer
