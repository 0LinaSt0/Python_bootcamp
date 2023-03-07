"""
Reaction evaluation:
	1. Respiration [norm is 12-16]:
		* [12; 16] - a human
		* another - a replicant
	2. Heart rate [norm is 60-100]:
		* [60; 100] - a human
		* another - a replicant
	3. Blushing level [just 6 levels]:
		* [1; 3] - a replicant
		* [4; 6] - a human
	4. Pupillary dilation [from 2 to 8]:
		* [2; 4] - a replicant
		* [5; 8] - a human
"""

from Reaction import Reactions


class ReactionsDetector:
	"""ReactionsDetector  class is used for detecting replicants

		``Attributes``

		:param dict reactions: dict with reactions' grades
		:param int questions_counter: counter of asked questions
		:param class ReactionDetectorException: custom exception for 
			ReactionsDetector class

		``Methods``

		is_human()
			Gives human/replicant verdict

		check_respiration()
			Checks respondent's respiration

		check_heartRate()
			Checks respondent's heart rate

		check_blushingLevel()
			Checks respondent's blushing level
		
		check_pupillaryDilation()
			Checks respondent's pupillary dilation

	
	"""

	def __init__(self, reactions: dict, questions_counter: int):
		self.reactions_dict = reactions
		self.questions_counter = questions_counter


	class ReactionDetectorException(Exception):
		"""Custom exception for ReactionsDetector inherited from 
		Exception

			``Attributes``
			
			:param string message: exception message

		"""

		def __init__(self, message) -> None:
			super().__init__(message)


	def is_human(self):
		"""Gives human/replicant verdict
		"""

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
		"""Checks respondent's respiration
		"""

		return (
			1 if self.reactions_dict[Reactions.RESPIRATION] // self.questions_counter
			in range(12, 17) else -1
		)
	
	
	def check_heartRate(self):
		"""Checks respondent's heart rate
		"""

		return (
			1 if self.reactions_dict[Reactions.HEART_RATE] // self.questions_counter
			in range(60, 101) else -1
		)
	
	
	def check_blushingLevel(self):
		"""Checks respondent's blushing level
		"""

		return (
			-1 if self.reactions_dict[Reactions.BLUSHING_LEVEL] // self.questions_counter
			in range(1, 4) else 1
		)
	
	
	def check_pupillaryDilation(self):
		"""Checks respondent's pupillary dilation
		"""

		return (
			-1 if self.reactions_dict[Reactions.PUPILLARY_DILATION] // self.questions_counter
			in range(2, 5) else 1
		)