from Question import Question
from Answer import AnswersKeeper
from ReactionsDetector import ReactionsDetector
from Reaction import (
	Respiration,
	HeartRate,
	BlushingLevel,
	PupillaryDilation,
	ReactionsCounter
)


class Interviewer:
	"""Interviewer class is used for representing a interview process

		``Attributes``

		:param int questions_dict: dict with questions

		``Methods``

		interview_process()
			Asking, taking answer, take grade reaction

		verdict()
			Writes human/replicant verdict ti output

		ask_question()
			Qsks questions and takes answers

		grade_answer_reaction()
			Grades every reaction
		
		grade()
			Grades every reaction

	
	"""

	def __init__(self, questions_dict):
		self.answers = AnswersKeeper()
		self.grades_reactions = ReactionsCounter()
		self.questions = questions_dict
		self.questions_count = 0
	

	def interview_process(self):
		"""Asking, taking answer, take grade reaction
		"""

		for key in self.questions:
			try:
				self.ask_question(key)
				print("\t~.~.~.~.~.~.~.~.~.~.~\n")
				self.questions_count += 1
				self.grade_answer_reaction()
			except:
				continue

	
	def verdict(self):
		"""Writes human/replicant verdict ti output
		"""
		
		try:
			is_human_reactions = ReactionsDetector(
				self.grades_reactions.reactions, self.questions_count
			).is_human()
			print("\n\t~~~~~~~ Verdict ~~~~~~~")
			if is_human_reactions:
				print("YOU'R A HUMAN. YOU CAN BE FREE\n")
			else: 
				print("!DANGER! REPLICANT WAS DETECTED\n")
		except ReactionsDetector.ReactionDetectorException as e:
			print(e)



	def ask_question(self, key):
		"""Qsks questions and takes answers

			:param string key: key to question
		"""

		try:
			question = Question(self.questions_count + 1, key, self.questions[key])
			question.print_question()
			answer = question.ask_answer()
			self.answers.save_answer(key, answer.num_answer)
		except Question.QuestionException as e:
			print(e)
			raise e


	def grade_answer_reaction(self):
		"""Grades every reaction
		"""
		
		print("I SEE. YOUR ...")
		reaction = Respiration()
		self.grade(reaction)
		
		reaction = HeartRate()
		self.grade(reaction)
		
		reaction = BlushingLevel()
		self.grade(reaction)

		reaction = PupillaryDilation()
		self.grade(reaction)


	def grade(self, reaction):
		"""Grades every reaction

			:param Reaction reaction: object of concret reaction
		"""
		
		reaction.grade_reaction()
		self.grades_reactions.update_reaction(reaction.evaluated, reaction.grade)
