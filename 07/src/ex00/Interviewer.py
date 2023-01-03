from Question import Question
from Answer import AswersKeeper
from Reaction import (
	Respiration,
	HeartRate,
	BlushingLevel,
	PupillaryDilation,
	ReactionsCounter,
	ReactionsDetector
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
		print("\t ~~~~~~~ Verdict ~~~~~~~")
		try: 
			is_human_reactions = ReactionsDetector(self.grades_reactions).is_human()
			if is_human_reactions:
				print("YOU'R A HUMAN. YOU CAN BE FREE")
			else: 
				print("!DANGER! REPLICANT WAS DETECTED")
		except ReactionsDetector.ReactionDetectorException as e:
			print(e)


	def ask_question(self, key):
		question = Question(key, self.questions[key])
		try:
			question.print_question()
			answer = question.ask_answer()
			self.answers.save_answer(key, answer)
		except Question.QuestionException as e:
			print(e)


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
