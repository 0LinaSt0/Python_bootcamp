"""
It swaps sender and receiver for the transaction
if there are account numbers of bad guys in coming messages
"""
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
