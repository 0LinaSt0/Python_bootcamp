
"""
Reactions evaluation:
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


from customException import customException


class Reactions:
	def __init__(self):
		self.reactions = {
			"respiration": 0,
			"heart_rate": 0,
			"blushing_level": 0,
			"pupillary_dilation": 0
		}
		self.is_input_correct = False


	def degree(self, what_estimate, ft_for_check_reaction):
		while self.is_input_correct == False:
			grade_reaction = input("{}: ".format(what_estimate))
			self.checker(grade_reaction, ft_for_check_reaction)
		self.is_input_correct = False


	def checker(self, grade_reaction, ft_for_check_reaction):
		try:
			grade_reaction = int(grade_reaction)
			if (grade_reaction < 0):
				raise customException
			ft_for_check_reaction(grade_reaction)
		except:
			print("!INCORRECTLY!")
		else:
			self.is_input_correct = True


	def check_respiration(self, grade_reaction):
		self.reactions["respiration"] += grade_reaction


	def check_heartRate(self, grade_reaction):
		self.reactions["heart_rate"] += grade_reaction


	def check_blushingLevel(self, grade_reaction):
		self.reactions["blushing_level"] += grade_reaction
		if grade_reaction not in range(1, 7):
			raise customException("\nError: out of range\n")


	def check_pupillaryDilation(self, grade_reaction):
		self.reactions["pupillary_dilation"] += grade_reaction
		if grade_reaction not in range(2, 9):
			raise customException("\nError: out of range\n")


	def is_respiration_norm(self, questions_counter):
			try:
				return (1 if self.reactions["respiration"] // questions_counter
						in range(12, 17) else -1)
			except:
				raise customException("\nError: something wrong [check Reactions.is_respiration_norm()]\n")


	def is_heartRate_norm(self, questions_counter):
		try:
			return (1 if self.reactions["heart_rate"] // questions_counter
					in range(60, 101) else -1)
		except:
			raise customException("\nError: something wrong [check Reactions.is_heartRate_norm()]\n")


	def is_blushingLevel_norm(self ,questions_counter):
		try:
			return (-1 if self.reactions["blushing_level"] // questions_counter
					in range(1, 4) else 1)
		except:
			raise customException("\nError: something wrong [check Reactions.is_blushingLevel_norm()]\n")


	def is_pupillaryDilation_norm(self ,questions_counter):
		try:
			return (-1 if self.reactions["pupillary_dilation"] // questions_counter
					in range(2, 5) else 1)
		except:
			raise customException("\nError: something wrong [check Reactions.is_pupillaryDilation_norm()]\n")


