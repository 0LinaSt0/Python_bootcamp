"""
Answer evaluation:
	1. it's definitely a replicant (1 score)
	2. it's could be a human or a replicant (2 score)
	3. it's definitely a human (3 score)



"""

class Answer:
	"""Answer class is used for representing a answer of respondent


	``Attributes``

	:param string question: asked question
	:param dict answer_options: dict with possible variants of answers
	:param class AnswerException: custom exception for Answer class

	``Methods``

	take_answer()
		Takes answer from respondent

	read_input()
		Reads answer from standart input

	check_answer()
		Checks respondent's answer for validity

	
	"""

	def __init__(self, question, answer_options: dict):
		self.question = question
		self.answer_options = answer_options
		self.is_valid = False
		self.num_answer: int


	class AnswerException(Exception):
		"""Custom exception for Answer inherited from Exception

		``Attributes``
		
		:param string message: exception message

		"""

		def __init__(self, message) -> None:
			super().__init__(message)


	def take_answer(self):
		"""Takes answer from respondent: looping until answer willn't be valid
		"""
		
		while not self.is_valid:
			try:
				self.read_input()
				self.check_answer()
			except:
				print("\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m")

	
	def read_input(self):
		"""Reads answer from standart input: expects just integers

		:raise Answer.AnswerException: if answer isn't integer
		"""

		try:
			self.num_answer = int(input("\nPLEASE, GIVE ME NUMBER OF ANSWER (INT): "))
		except:
			raise Answer.AnswerException("\nError: invalid input\n")


	def check_answer(self):
		"""
		Checks respondent's answer for validity: answer could be just 
		number of possible variants of answers

		:raise Answer.AnswerException: if answer out of range


		"""

		if self.num_answer not in range(1, (len(self.answer_options) + 1)):
			raise Answer.AnswerException("\nError: out of range\n")
		self.is_valid = True



class AnswersKeeper:
	"""AnswersKeeper class is keeping given respondent's answers

	``Methods``
	
	save_answer()
		Appends answer to dict of answers
	"""

	def __init__(self):
		self.answers = {}

	
	def save_answer(self, question, answer):
		"""Appends answer to dict of answers: inserts new answer
		"""

		self.answers[question] = answer
