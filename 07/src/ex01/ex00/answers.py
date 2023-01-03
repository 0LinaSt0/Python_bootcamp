"""
Answer evaluation:
	1 - it's definitely a replicant (1 score)
	2 - it's could be a human or a replicant (2 score)
	3 - it's definitely a human (3 score)

	scorses:
	a) [10; 20) - a replicant
	b) [20; 30] - a human
"""


import json
from customException import customException


class Answer:
	def __init__(self):
		self.answers = {}


	def write_answers(self):
		json_object = json.dumps(self.answers, indent=4)
		with open("answers.json", "w") as outfile:
			outfile.write(json_object)
		return json_object


	def append_answer(self, index):
		num_answer = input("PLEASE, GIVE ME NUMBER OF ANSWER (INT): ")
		self.check_answer(index, num_answer)


	def check_answer(self, index, num_answer):
		try:
			num_answer = int(num_answer)
			if num_answer not in range(1, 4):
				raise customException("\nError: out of range\n")
			print("CORRECTLY")
		except:
			print("!INCORRECTLY!")


	def is_human(self):
		return (-1 if sum(self.answers.values()) in range(10, 20) else 1)
