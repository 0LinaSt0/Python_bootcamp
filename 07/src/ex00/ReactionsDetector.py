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

from Reaction import Reactions

class ReactionsDetector:
	def __init__(self, reactions: dict, questions_counter: int):
		self.reactions_dict = reactions
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
			1 if self.reactions_dict[Reactions.RESPIRATION] // self.questions_counter
			in range(12, 17) else -1
		)
	
	
	def check_heartRate(self):
		return (
			1 if self.reactions_dict[Reactions.HEART_RATE] // self.questions_counter
			in range(60, 101) else -1
		)
	
	
	def check_blushingLevel(self):
		return (
			-1 if self.reactions_dict[Reactions.BLUSHING_LEVEL] // self.questions_counter
			in range(1, 4) else 1
		)
	
	
	def check_pupillaryDilation(self):
		return (
			-1 if self.reactions_dict[Reactions.PUPILLARY_DILATION] // self.questions_counter
			in range(2, 5) else 1
		)