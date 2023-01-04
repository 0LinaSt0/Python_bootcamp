from Answer import Answer


class Question:
	def __init__(self, question_num: int, question, answer_options: dict):
		self.question_num = question_num
		self.question = question 
		self.answer_options = answer_options


	class QuestionException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def print_question(self):
		if len(self.answer_options) <= 0:
			raise Question.QuestionException("\nError: answer options are missing\n")
		print("\n{}. {}".format(self.question_num, self.question))
		for answer in self.answer_options:
			print("\t{}) {}".format(answer, self.answer_options[answer]))


	def ask_answer(self):
		answer = Answer(self.question, self.answer_options)
		answer.take_answer()
		return answer