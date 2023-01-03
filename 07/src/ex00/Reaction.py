"""
Reaction evaluation:
	1. Respiration [norm is 12-16]:
		a) [12; 16] - a human
		b) another - a replicant
	2. Heart rate [norm is 60-100]:
		a) [60; 100] - a human
		b) another - a replicant
	3. Blushing level [just 6 levels]:
		a) [1; 3] - a replicant
		b) [4; 6] - a human
	4. Pupillary dilation [from 2 to 8]:
		a) [2; 4] - a replicant
		b) [5; 8] - a human
"""

from enum import Enum


class Reactions(Enum):
	DEFAULT = "default"
	RESPIRATION = "respiration"
	HEART_RATE = "heart_rate"
	BLUSHING_LEVEL = "blushing_level"
	PUPILLARY_DILATION = "pupillary_dilation"


class Reaction:
	def __init__(self):
		self.grade: int
		self.evaluated = Reactions.DEFAULT
		self.is_valid = False


	class ReactionException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def grade_reaction(self):
		print("AAAAAAAA: ", self.is_valid)
		while not self.is_valid:
			self.read_input()
			self.check_grade()


	def read_input(self):
		try:
			self.grade = int(input("{}: ".format(self.evaluated.value)))
		except:
			print("\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m")

	def check_grade(self):
		try:
			if (self.grade < 0):
				raise Reaction.ReactionException("\nError: out of range\n")
			self.check_conditions()
			self.is_valid = True
		except:
			print("\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m")


	def check_conditions(safe):
		pass


class Respiration(Reaction):
	def __init__(self):
		self.evaluated = Reactions.RESPIRATION


class HeartRate(Reaction):
	def __init__(self):
		self.evaluated = Reactions.HEART_RATE


class BlushingLevel(Reaction):
	def __init__(self):
		self.evaluated = Reactions.BLUSHING_LEVEL


	def check_conditions(self):
		if self.grade not in range(1, 7):
			raise Reaction.ReactionException("\nError: out of range\n")


class PupillaryDilation(Reaction):
	def __init__(self):
		self.evaluated = Reactions.PUPILLARY_DILATION


	def check_conditions(self):
		if self.grade not in range(2, 9):
			raise Reaction.ReactionException("\nError: out of range\n")




class ReactionsCounter:
	def __init__(self):
		self.reactions = {
			Reactions.RESPIRATION: 0,
			Reactions.HEART_RATE: 0,
			Reactions.BLUSHING_LEVEL: 0,
			Reactions.PUPILLARY_DILATION: 0
		}

	
	def update_reaction(self, reaction: Reactions, update_sum: int):
		self.reactions[reaction] += update_sum




class ReactionsDetector:
	def __init__(self, reactions: dict, questions_counter: int):
		self.reactions_dist = reactions
		self.questions_counter = questions_counter


	class ReactionDetectorException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def is_human(self):
		try:
			verdict = (
				self.check_respiration() 
				+ self.check_heartRate()
				+ self.check_blushingLevel()
				+ self.check_pupillaryDilation()
			)
			return (False if verdict < 0 else True)
		except:
			raise ReactionsDetector.ReactionDetectorException(
				"\nError: something wrong: check arguments in ReactionsDetector.is_reaction_norm\n"
			)

	
	def check_respiration(self):
		return (
			1 if self.reactions_dist[Reactions.RESPIRATION] // self.questions_counter
			in range(12, 17) else -1
		)
	
	
	def check_heartRate(self):
		return (
			1 if self.reactions_dist[Reactions.HEART_RATE] // self.questions_counter
			in range(60, 101) else -1
		)
	
	
	def check_blushingLevel(self):
		return (
			-1 if self.reactions_dist[Reactions.BLUSHING_LEVEL] // self.questions_counter
			in range(1, 4) else 1
		)
	
	
	def check_pupillaryDilation(self):
		return (
			-1 if self.reactions_dist[Reactions.PUPILLARY_DILATION] // self.questions_counter
			in range(2, 5) else 1
		)