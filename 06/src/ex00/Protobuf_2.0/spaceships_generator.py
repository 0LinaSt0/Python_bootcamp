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
	"Algeria",
	"UK",
	"Peru"
]


def ship_generator():
	alignment_status = random.choice(Spaceship.alignment)
	is_enemy = (alignment_status == Spaceship.alignment.ENEMY)
	officers_count = (random(0, 11) if is_enemy else random(1, 11))
	return Spaceship(
		alignment=alignment_status,
		name=(random.choice(SHIPS_NAMES + "Unknown")
				if is_enemy else random.choice(SHIPS_NAMES)
			),
		ship_class=random.choice(Spaceship.ship_class),
		length=round(random.uniform(150.50, 500,50), 1),
		crew_size=random(2, 15),
		armed=random.choice[True, False],
		officers=[ {
			Spaceship.officers.first_name: random.choice(OFFICERS_NAMES),
			Spaceship.officers.last_name: random.choice(OFFICERS_SURNAMES),
			Spaceship.officers.rang: random.choice(OFFICERS_RANGS)
			} for _ in range(officers_count)
		]
	)

