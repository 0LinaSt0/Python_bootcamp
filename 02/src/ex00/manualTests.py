from key import Key


"""TESTS_CODE"""
if __name__ == "__main__":
	key = Key()

	print("1. len(key) == 1337\t\t\t-> {}\t-> [UNLOCK]".format(len(key) == 1337))
	print("2. key[404] == 3\t\t\t-> {}\t-> [UNLOCK]".format(key[404] == 3))
	print("3. key > 9000\t\t\t\t-> {}\t-> [UNLOCK]".format(key > 9000))
	print("4. key.passphrase == \"zax2rulez\"\t-> {}\t-> [UNLOCK]".format(key.passphrase == "zax2rulez"))
	print("5. str(key) == \"GeneralTsoKeycard\"\t-> {}\t-> [UNLOCK]".format(str(key) == "GeneralTsoKeycard"))
