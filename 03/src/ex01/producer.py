"""
{
   "metadata": {
       "from": 1023461745,
       "to": 5738456434
   },
   "amount": 10000
}

myList = [{'a': 54}, {'b': 41, 'c':87}]
jsonString = json.dumps(myList, indent=4)
print(jsonString)

"""
import json
import redis
import random
import time

class messagesGenerator:

	def __init__(self):
		self.an_from = self.an_to = self.amount = 0

	def testsExample(self):
		message1 = {"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 1000}
		message2 = {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}
		message3 = {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}
		ret = [json.dumps(message1, indent=4), json.dumps(message2, indent=4), json.dumps(message3, indent=4)]
		return ret

	def informationGenerator(self):
		self.an_from = random.randint(1000000000, 10000000000)
		self.an_to = random.randint(1000000000, 10000000000)
		self.amount = random.randint(-5001, 5001)

	def generateMessage(self):
		self.informationGenerator()
		message = {"metadata": {"from": self.an_from, "to": self.an_to}, "amount": self.amount}
		jsonConvert = json.dumps(message, indent=4)
		#print(self.an_from, self.an_to, self.amount)
		return jsonConvert


def producer():
	a = messagesGenerator()
	r = redis.Redis()
	iter_for_tests = 0

	# For sending messages
	while True:
		while iter_for_tests < 3:
			r.publish("channel1", a.testsExample()[iter_for_tests])
			iter_for_tests += 1
			time.sleep(5)
		r.publish("channel1", a.generateMessage())
		time.sleep(5)



#EXEC
producer()