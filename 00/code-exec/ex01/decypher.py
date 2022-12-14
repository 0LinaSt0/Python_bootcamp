"""
The script returns names of famous GB places which are generated
using every first letter of words (coming to input as string)

Variants for running the script:
	~$ python decypher.py "Have you delivered eggplant pizza at restored keep?"
	~$ python decypher.py "The only way everyone reaches Brenda rapidly is delivering groceries explicitly"
	~$ python decypher.py "Britain is Great because everyone necessitates"
"""

import sys

if "__main__" == __name__:
	if len(sys.argv) != 2:
		print("Please, give me one message for decrypting")
	else:
		# a split method splits string's elements
		input_words = (elem for elem in sys.argv[1].split())
		for word in input_words:
			print(word[0], end = '')
		print('')
