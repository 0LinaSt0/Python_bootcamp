from enum import Enum


class Reactions(Enum):
	"""Reactions class is enum with different reactions

		``Attributes``
		
		:param string DEFAULT: default
		:param string RESPIRATION: respiration
		:param string HEART_RATE: heart rate
		:param string BLUSHING_LEVEL: blushing level [1, 6]
		:param string PUPILLARY_DILATION: pupillary dilation [2, 8]

	"""

	DEFAULT = "default"
	RESPIRATION = "respiration"
	HEART_RATE = "heart rate"
	BLUSHING_LEVEL = "blushing level [1, 6]"
	PUPILLARY_DILATION = "pupillary dilation [2, 8]"


class Reaction:
	"""Reaction parent class is used for representing a reactions for 
	children

		``Attributes``

		:param int grade: drade of reaction
		:param enum evaluated: enum of Reactions
		:param bool is_valid: flag for checking valid grade
		:param class ReactionException: custom exception for Reaction class

		``Methods``

		grade_reaction()
			Grades respondent's reaction

		read_input()
			Reads gave reaction

		check_grade()
			Checks that gave reaction is valid

		check_conditions()
			Check special conditions for concret reaction

	
	"""

	def __init__(self):
		self.grade: int
		self.evaluated = Reactions.DEFAULT
		self.is_valid = False


	class ReactionException(Exception):
		"""Custom exception for Reaction inherited from Exception

		``Attributes``
		
		:param string message: exception message

		"""

		def __init__(self, message) -> None:
			super().__init__(message)


	def grade_reaction(self):
		"""Grades respondent's reaction
		"""

		while not self.is_valid:
			try:
				self.read_input()
				self.check_grade()
			except:
				print("\x1b[2;33m" + "!INCORRECTLY!" + "\x1b[0m")


	def read_input(self):
		"""Reads gave reaction

		:raise Reaction.ReactionException: if invalid input
		"""
		
		try:
			self.grade = int(input("{}: ".format(self.evaluated.value)))
		except:
			raise Reaction.ReactionException("\nError: invalid input\n")


	def check_grade(self):
		"""Checks that gave reaction is valid

		:raise Reaction.ReactionException: if grade out of range
		"""

		if (self.grade < 0):
			raise Reaction.ReactionException("\nError: out of range\n")
		self.check_conditions()
		self.is_valid = True


	def check_conditions(safe):
		"""Check special conditions for concret reaction: implementing 
		in children classes
		"""

		pass


class Respiration(Reaction):
	"""Respiration child class is used for representing a respiration
	reaction
	"""

	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.RESPIRATION


class HeartRate(Reaction):
	"""Respiration child class is used for representing a heart rate
	reaction
	"""
	
	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.HEART_RATE


class BlushingLevel(Reaction):
	"""BlushingLevel child class is used for representing a blushing level
	reaction

	``Methods``

	check_conditions()
		Check special conditions for blushing level reaction
	
	"""

	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.BLUSHING_LEVEL


	def check_conditions(self):
		"""Check special conditions for blushing level reaction
		"""

		if self.grade not in range(1, 7):
			raise Reaction.ReactionException("\nError: out of range\n")


class PupillaryDilation(Reaction):
	"""PupillaryDilation child class is used for representing 
	a pupillary dilation reaction

	``Methods``

	check_conditions()
		Check special conditions for pupillary dilation reaction
	
	"""

	def __init__(self):
		super().__init__()
		self.evaluated = Reactions.PUPILLARY_DILATION


	def check_conditions(self):
		"""Check special conditions for pupillary dilation reaction
		"""

		if self.grade not in range(2, 9):
			raise Reaction.ReactionException("\nError: out of range\n")




class ReactionsCounter:
	"""ReactionsCounter class is counting grade reactions

	``Methods``
	
	update_reaction()
		Regrade passing reaction
	"""

	def __init__(self):
		self.reactions = {
			Reactions.RESPIRATION: 0,
			Reactions.HEART_RATE: 0,
			Reactions.BLUSHING_LEVEL: 0,
			Reactions.PUPILLARY_DILATION: 0
		}

	
	def update_reaction(self, reaction: Reactions, update_sum: int):
		"""Regrade passing reaction

		:param class reaction: changed reaction
		:param int update_sum: how much to increase changed reaction
		"""

		self.reactions[reaction] += update_sum