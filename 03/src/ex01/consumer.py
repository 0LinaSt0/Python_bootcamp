"""
GREATE TUTORIALS:
1. https://koalatea.io/python-redis-pubsub/
2. https://kb.objectrocket.com/redis/basic-redis-usage-example-part-2-pub-sub-in-depth-using-redis-python-719
"""

import redis
import time
import json
import argparse

class updateMessages:

	def __init__(self):
		self.updating = {}

	def RobinHood(self, data, args):
		r_data = data.copy()

		if str(r_data["metadata"]["to"]) in args and int(r_data["amount"]) > 0:
			tmp = r_data["metadata"]["from"]
			r_data["metadata"]["from"] = r_data["metadata"]["to"]
			r_data["metadata"]["to"] = tmp
		return r_data


def counsumer(inp):
	a = updateMessages()
	# Create redis object
	r = redis.Redis()
	# Create pubsub object
	p = r.pubsub()

	# Subscribe two channels
	p.subscribe("channel1")

	# Waiting signal loop
	while True:
		message = p.get_message()
		if message and message.get("type") == "message":
			print(a.RobinHood(json.loads(message.get("data")), inp))
			#print(json.loads(message.get("data")).get("metadata"))
		time.sleep(0.01)



#EXEC
parser = argparse.ArgumentParser(description="Ping script")
parser.add_argument('-e', dest="inp", type=str)
args = parser.parse_args()

counsumer(list(args.inp.split(',')))

