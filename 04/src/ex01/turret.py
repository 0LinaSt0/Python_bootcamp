from random import randint
from typing import Dict


LIST_ATRIBUTS = [
	"neuroticism",
	"openness",
	"conscientiousness",
	"extraversion",
	"agreeableness"
	]


ATRIBUTS_SUM = 100


def shoot(self):
	print("Shooting")


def search(self):
	print("Searching")


def talk(self):
	print("Talking")


def take_atributs() -> Dict[str, int]:
	print("take_atributs")
	result = {}
	reminder = ATRIBUTS_SUM
	for elem in LIST_ATRIBUTS[:-1]:
		part = randint(0, reminder)
		result[elem] = part
		reminder -= part
	result[LIST_ATRIBUTS[-1]] = reminder
	return result


def take_methods():
	print("take_methods")
	return {
		"shoot": shoot, 
		"search": search, 
		"talk": talk
		}

