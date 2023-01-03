from json import load
from customException import customException


class Questions:
	def __init__(self, question_path):
		self.questions_dict = self.take_questions(question_path)
		self.questions_count = len(self.questions_dict)


	def take_questions(self, question_path):
		try:
			with open(question_path, "r") as openfile:
				log = load(openfile)
				print("Success creating")
				return log
		except:
			raise customException("\nError: file \"{}\" cannot be executed\n".format(question_path))

	def out_questions(self):
		return (question for question in self.questions_dict)