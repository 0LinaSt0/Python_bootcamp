from Answer import Answer


class Question:
	"""Question class is used for representing a question

	``Attributes``

	:param int question_num: number of question
	:param string question: question
	:param dict answer_options: dict with possible variants of answers
	:param class AnswerException: custom exception for Answer class

	``Methods``

	print_question()
		Prints question to output

	ask_answer()
		Asks answer from respondent

	
	"""

	def __init__(self, question_num: int, question, answer_options: dict):
		self.question_num = question_num
		self.question = question 
		self.answer_options = answer_options


	class QuestionException(Exception):
		"""Custom exception for Question inherited from Exception

		``Attributes``
		
		:param string message: exception message

		"""
		
		def __init__(self, message) -> None:
			super().__init__(message)


	def print_question(self):
		"""Prints question to output

		:raise Answer.AnswerException: if answer options are missing
		"""
		if len(self.answer_options) <= 0:
			raise Question.QuestionException("\nError: answer options are missing\n")
		print("\n{}. {}".format(self.question_num, self.question))
		for answer in self.answer_options:
			print("\t{}) {}".format(answer, self.answer_options[answer]))


	def ask_answer(self):
		"""Asks answer from respondent

		:return: the Answer object class
		:rtype: Answer
		"""
		answer = Answer(self.question, self.answer_options)
		answer.take_answer()
		return answer