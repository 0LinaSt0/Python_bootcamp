# personality traits: neuroticism, openness, conscientiousness, extraversion, agreeableness
# actions: shoot, search, talk

from turret import take_atributs
from turret import take_methods
from time import sleep

def turrets_generator():
	while True:
		yield type("Turret", (object,), dict(take_atributs() | take_methods()))()


if __name__ == "__main__":
	for turret, _ in zip(turrets_generator(), range(10)):
		l_personalities = [
			turret.neuroticism, 
			turret.openness, 
			turret.conscientiousness, 
			turret.extraversion,
			turret.agreeableness
			]
		print("personalities: ", l_personalities)
		print("sum of personalities: ", sum(l_personalities))
		turret.shoot()
		turret.search()
		turret.talk()
		print("\n")
		sleep(1)

