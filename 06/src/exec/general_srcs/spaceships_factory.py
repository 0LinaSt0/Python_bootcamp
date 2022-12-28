import random, sys
sys.path.insert(1, "proto_srcs/")
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

OFFICERS_RANKS = [
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


def officer_factory():
	officer = Officer()
	officer.first_name = random.choice(OFFICERS_NAMES)
	officer.last_name = random.choice(OFFICERS_SURNAMES)
	officer.rank = random.choice(OFFICERS_RANKS)
	return officer


def ship_factory():
	alignment_status = random.choice(Alignment.keys())
	is_enemy = (alignment_status == Alignment.Enemy)
	officers_count = random.randrange(0, 11) if is_enemy else random.randrange(1, 11)

	random_spaceship = Spaceship()
	random_spaceship.alignment = alignment_status
	random_spaceship.name = (random.choice(SHIPS_NAMES + ["Unknown"])
								if is_enemy else random.choice(SHIPS_NAMES))
	random_spaceship.ship_class = random.choice(Class.keys())
	random_spaceship.length = round(random.uniform(150.50, 500.50), 1)
	random_spaceship.crew_size = random.randrange(2, 15)
	random_spaceship.armed = random.choice([True, False])
	for _ in range(officers_count):
		random_spaceship.officers.append(officer_factory())
	return random_spaceship




# For checking
from json import loads
from google.protobuf.json_format import MessageToJson


if __name__ == "__main__":
	json_obj = loads('{"key": "value", "kkk": "vvv"}')
	print(type(json_obj))
	print(json_obj)
	"""
	json_obj = MessageToJson(ship_factory())
	print(json_obj)
	with open('json_data.json', 'w') as outfile:
		outfile.write(json_obj)
	"""
