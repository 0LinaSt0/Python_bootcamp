import random
from spaceships_pb2 import (
	Alignment,
	Class,
	Officer,
	Spaceship
)

OFFICERS_NAMES = [
	"Alan",
	"Laan",
	"Aaln",
	"Nala"
]

OFFICERS_SURNAMES = [
	"Shepard",
	"Epaedsh",
	"Pardesh",
	"Epshard"
]

OFFICERS_RANGS = [
	"Commander",
	"Major",
	"Captain",
	"Lieutenant"
]

SHIPS_NAMES = [
	"Normandy",
	"Albania",
	"Ingria",
	"UK",
	"Peru"
]


def officeres_generator():
	officer = Officer()
	officer.first_name = random.choice(OFFICERS_NAMES)
	officer.last_name = random.choice(OFFICERS_SURNAMES)
	officer.rank = random.choice(OFFICERS_RANGS)
	return {
		"first_name": officer.first_name,
		"last_name": officer.last_name,
		"rank": officer.rank
	}


def ship_generator():
	alignment_status = random.choice(list(Alignment))
	is_enemy = (alignment_status == Alignment.ENEMY)
	officers_count = (random(0, 11) if is_enemy else random(1, 11))

	random_spaceship = Spaceship()
	random_spaceship.alignment = alignment_status
	random_spaceship.name = (random.choice(SHIPS_NAMES + ["Unknown"])
								if is_enemy else random.choice(SHIPS_NAMES))
	random_spaceship.ship_class = random.choice(Class),
	random_spaceship.length = round(random.uniform(150.50, 500.50), 1),
	random_spaceship.crew_size = random(2, 15),
	random_spaceship.armed = random.choice[True, False],
	(random_spaceship.officers.extend(officeres_generator()) for _ in range(officers_count))
	return random_spaceship


"""
from enum import Enum

class AAA (Enum):
	ALLY = 0
	ENEMY = 1


if __name__ == "__main__":
	b = random.choice(list(AAA))
	print(b)
"""
