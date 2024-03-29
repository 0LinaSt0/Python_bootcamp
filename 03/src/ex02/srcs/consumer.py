"""
GREATE TUTORIALS:
1. https://koalatea.io/python-redis-pubsub/
2. https://kb.objectrocket.com/redis/basic-redis-usage-example-part-2-pub-sub-in-depth-using-redis-python-719
"""

"""
Start consumer:
	python3 consumer.py -e 7134456234,3476371234
"""

from redis import Redis
from time import sleep
from json import loads
from argparse import ArgumentParser

import logging


class updateMessages:

	def __init__(self):
		self.updating = {}


	def RobinHood(self, data, args):
		r_data = data.copy()

		if str(r_data["metadata"]["to"]) in args and int(r_data["amount"]) > 0:
			tmp = r_data["metadata"]["from"]
			r_data["metadata"]["from"] = r_data["metadata"]["to"]
			r_data["metadata"]["to"] = tmp
			print()
			logging.basicConfig(level=logging.INFO)
			logging.info(f'ACCOUNT NUMBERES WAS CHANGED: {r_data["metadata"]["from"]} <-> {r_data["metadata"]["to"]}')
		return r_data


def counsumer(inp):
	messagerUpdater = updateMessages()
	# Create redis object
	r = Redis()
	# Create pubsub object which returns the number matching channel and pattern subscriptions
	pub = r.pubsub()

	# Subscribe two channel1
	pub.subscribe("channel1")

	# Waiting signal loop
	while True:
		message = pub.get_message()
		if message and message.get("type") == "message":
			print(messagerUpdater.RobinHood(loads(message.get("data")), inp))
			#print(loads(message.get("data")).get("metadata"))
		sleep(0.01)



#EXEC
if __name__ == "__main__":
	parser = ArgumentParser(description="Ping script")
	# Add flag -e
	parser.add_argument('-e', dest="inp", type=str)
	# Create parser for arguments object
	args = parser.parse_args()

	# Create list with two coming account numbers
	counsumer(list(args.inp.split(',')))

