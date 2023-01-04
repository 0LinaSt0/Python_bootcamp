from Question import Question
from Answer import AswersKeeper
from ReactionsDetector import ReactionsDetector
from Reaction import (
	Respiration,
	HeartRate,
	BlushingLevel,
	PupillaryDilation,
	ReactionsCounter
)


class Interviewer:
	def __init__(self, questions_dict):
		self.answers = AswersKeeper()
		self.grades_reactions = ReactionsCounter()
		self.questions = questions_dict
		self.questions_count = 0
	

	def interview_process(self):
		for key in self.questions:
			try:
				self.ask_question(key)
				print("\t~.~.~.~.~.~.~.~.~.~.~\n")
				self.grade_answer_reaction()
				self.questions_count += 1
			except:
				continue

	
	def verdict(self):
		print("\n\t~~~~~~~ Verdict ~~~~~~~")
		try:
			is_human_reactions = ReactionsDetector(
				self.grades_reactions.reactions, self.questions_count
				).is_human()
			if is_human_reactions:
				print("YOU'R A HUMAN. YOU CAN BE FREE\n")
			else: 
				print("!DANGER! REPLICANT WAS DETECTED\n")
		except ReactionsDetector.ReactionDetectorException as e:
			print(e)


	def ask_question(self, key):
		question = Question(self.questions_count + 1, key, self.questions[key])
		try:
			question.print_question()
			answer = question.ask_answer()
			self.answers.save_answer(key, answer.num_answer)
		except Question.QuestionException as e:
			print(e)
			raise e


	def grade_answer_reaction(self):
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
		reaction.grade_reaction()
		self.grades_reactions.update_reaction(reaction.evaluated, reaction.grade)
