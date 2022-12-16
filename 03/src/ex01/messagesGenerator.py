"""
- JSON structure which should be generated:
	{
		"metadata": {
			"from": 1023461745,
			"to": 5738456434
		},
		"amount": 10000
	}
"""

from json import dumps
from random import randint


class messagesGenerator:

	def __init__(self):
		self.an_from = self.an_to = self.amount = 0


	def testsExample(self):
		message1 = {"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 1000}
		message2 = {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}
		message3 = {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}
		# convert messages to JSON format
		ret = [dumps(message1, indent=4), dumps(message2, indent=4), dumps(message3, indent=4)]
		return ret


	def informationGenerator(self):
		# Generate random account numbers
		self.an_from = randint(1000000000, 10000000000)
		self.an_to = randint(1000000000, 10000000000)
		self.amount = randint(-5001, 5001)


	def generateMessage(self):
		self.informationGenerator()
		message = {"metadata": {"from": self.an_from, "to": self.an_to}, "amount": self.amount}
		jsonConvert = dumps(message, indent=4)
		#print(self.an_from, self.an_to, self.amount)
		return jsonConvert
