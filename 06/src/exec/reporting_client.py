# ~$ ./reporting_client.py 17 45 40.0409 −29 00 28.118
import sys
from json import dumps, loads
sys.path.insert(1, "./general_srcs/")
from utils import ft_request


def to_json_file(list_obj):
	with open("reply_data.json", 'w') as outfile:
		outfile.write(dumps(list_obj, indent=4))


def json_reply(dict_obj):
	json_obj = dumps(dict_obj["responsShips"], indent=4)
	print(json_obj)
	return loads(json_obj)


def reply_handler(message: dict):
	return json_reply(message)


if "__main__" == __name__:
	input_coordinates = sys.argv[1]

	to_json_file(ft_request(input_coordinates, reply_handler))
