# ~$ ./reporting_client_v2.py 17 45 40.0409 −29 00 28.118
import sys
from json import dumps, loads
from ValidateSpaceships import ValidateSpaceships
from pydantic import ValidationError
sys.path.insert(1, "./general_srcs/")
from utils import ft_request, to_json_file


def json_reply(dict_obj):
	return dumps(dict_obj["responsShips"], indent=4)


def reply_valid_handler(message: dict):
	json_obj = json_reply(message)
	json_load = loads(json_obj)
	try:
		ValidateSpaceships.parse_obj(json_load)
		print(json_obj)
		return json_load
	except ValidationError as err:
		return {"ERROR": err.json()} | json_load

if __name__ == "__main__":
	input_coordinates = sys.argv[1]

	to_json_file(ft_request(input_coordinates, reply_valid_handler))
