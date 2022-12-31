from json import load


class Questions:
	def __init__(self, question_path):
		self.questions_dict = self.take_questions(question_path)
		self.questions_count = len(self.questions_dict)


	def take_questions(self, question_path):
		try:
			with open(question_path, "r") as openfile:
				print("Success creating")
				return load(openfile)
		except:
			print("File \"{}\" didn't exec".format(question_path))
			return {}

	def out_questions(self):
		return (question for question in self.questions_dict)
