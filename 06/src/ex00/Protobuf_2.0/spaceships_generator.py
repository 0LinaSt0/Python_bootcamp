import random
from spaceships_pb2 import Spaceship

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
	officer = Spaceship.Officer()
	officer.first_name = random.choice(OFFICERS_NAMES)
	officer.last_name = random.choice(OFFICERS_SURNAMES)
	officer.rank = random.choice(OFFICERS_RANGS)
	return {
		"first_name": officer.first_name,
		"last_name": officer.last_name,
		"rank": officer.rank
	}


def ship_generator():
	alignment_status = random.choice(Spaceship.Alignment)
	is_enemy = (alignment_status == Spaceship.Alignment.ENEMY)
	officers_count = (random(0, 11) if is_enemy else random(1, 11))
	return Spaceship(
		alignment=alignment_status,
		name=(random.choice(SHIPS_NAMES + ["Unknown"])
				if is_enemy else random.choice(SHIPS_NAMES)),
		ship_class=random.choice(Spaceship.Class),
		length=round(random.uniform(150.50, 500.50), 1),
		crew_size=random(2, 15),
		armed=random.choice[True, False],
		officers=[officeres_generator() for _ in range(officers_count)]
	)


