from json import dumps

class Writer:
	def __init__(self, path, data):
		self.path = path
		self.data = data

	
	def write_to_file(self):
		json_object = dumps(self.data, indent=4)
		with open(self.path, "w") as outfile:
			outfile.write(json_object)