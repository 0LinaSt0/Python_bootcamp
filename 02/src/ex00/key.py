"""
~~~~~~~~~~~~~GENERAL_RULS~~~~~~~~~~~~~
AssertionError: len(key) == 1337
AssertionError: key[404] == 3
AssertionError: key > 9000
AssertionError: key.passphrase == "zax2rulez"
AssertionError: str(key) == "GeneralTsoKeycard"
"""

class Key:
	def __init__(self):
		self.passphrase = "zax2rulez"

	def __len__(self):
		return 1337

	def __getitem__(self, index):
		if index == 404:
			return 3
		return 0

	def __gt__(self, other):
		if other <= 9000:
			return True
		return False

	def __str__(self):
		return f"GeneralTsoKeycard"



"""TESTS_CODE"""
if __name__ == "__main__":
	key = Key()

	print("1. len(key) == 1337			-> ", len(key) == 1337, "-> [UNLOCK]")
	print("2. key[404] == 3			-> ", key[404] == 3, "-> [UNLOCK]")
	print("3. key > 9000				-> ", key > 9000, "-> [UNLOCK]")
	print("4. key.passphrase == \"zax2rulez\"	-> ", key.passphrase == "zax2rulez", "-> [UNLOCK]")
	print("5. str(key) == \"GeneralTsoKeycard\"	-> ", str(key) == "GeneralTsoKeycard", "-> [UNLOCK]")

