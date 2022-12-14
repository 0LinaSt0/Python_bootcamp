import json


class Questions:
	def __init__(self):
		self.questions_dict = self.take_questions()
		self.questions_count = len(self.questions_dict)


	def take_questions(self):
		with open("questions.json", "r") as openfile:
			return json.load(openfile)


	def out_questions(self):
		return (question for question in self.questions_dict)
