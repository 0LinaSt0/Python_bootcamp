from enum import Enum


class Reactions(Enum):
	DEFAULT = "default"
	RESPIRATION = "respiration"
	HEART_RATE = "heart rate"
	BLUSHING_LEVEL = "blushing level [1, 6]"
	PUPILLARY_DILATION = "pupillary dilation [2, 8]"


class Reaction:
	def __init__(self):
		self.grade: int
		self.evaluated = Reactions.DEFAULT
		self.is_valid = False


	class ReactionException(Exception):
		def __init__(self, message) -> None:
			super().__init__(message)


	def grade_reaction(self):
		while not self.is_valid:
			try:
				self.read_input()
				self.check_grade()
			except:
				print("\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m")


	def read_input(self):
		try:
			self.grade = int(input("{}: ".format(self.evaluated.value)))
		except:
			raise Reaction.ReactionException("\nError: invalid input\n")


	def check_grade(self):
		if (self.grade < 0):
			raise Reaction.ReactionException("\nError: out of range\n")
		self.check_conditions()
		self.is_valid = True


	def check_conditions(safe):
		pass


class Respiration(Reaction):
	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.RESPIRATION


class HeartRate(Reaction):
	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.HEART_RATE


class BlushingLevel(Reaction):
	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.BLUSHING_LEVEL


	def check_conditions(self):
		if self.grade not in range(1, 7):
			raise Reaction.ReactionException("\nError: out of range\n")


class PupillaryDilation(Reaction):
	def __init__(self):
		super().__init__()
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