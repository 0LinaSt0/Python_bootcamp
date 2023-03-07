"""
personality traits: neuroticism, openness, conscientiousness, extraversion, agreeableness
actions: shoot, search, talk
"""


from turret import take_atributs, take_methods
from time import sleep


def turrets_generator():
	while True:
		#type function generates dynamic class
		yield type("Turret", (object,), dict(take_atributs() | take_methods()))()


if __name__ == "__main__":
	for turret, i in zip(turrets_generator(), range(1, 11)):
		print("TURRET_{}".format(i))
		personalities = [
			turret.neuroticism,
			turret.openness,
			turret.conscientiousness,
			turret.extraversion,
			turret.agreeableness
			]
		print("personalities: ", personalities)
		print("sum of personalities: ", sum(personalities))
		turret.shoot()
		turret.search()
		turret.talk()
		print("\n")
		sleep(2)

