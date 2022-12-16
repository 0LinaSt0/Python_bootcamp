from redis import Redis
from time import sleep
from messagesGenerator import messagesGenerator


"""
Producer generates JSON messages with account information
and sends it to "channel1" as a payload into a Redis pubsub queue.
"""
def producer():
	a = messagesGenerator()
	r = Redis()
	iter_for_tests = 0

	# Send message to "channel1"
	while True:
		while iter_for_tests < 3:
			r.publish("channel1", a.testsExample()[iter_for_tests])
			iter_for_tests += 1
			sleep(5)
		r.publish("channel1", a.generateMessage())
		sleep(5)



#EXEC
if __name__ == "__main__":
	producer()
