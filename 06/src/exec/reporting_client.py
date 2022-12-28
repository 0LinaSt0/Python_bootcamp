#! /usr/bin/env python3

# ~$ ./reporting_client.py 17 45 40.0409 −29 00 28.118
import sys
import argparse
from json import loads, dumps
sys.path.insert(1, "./general_srcs/")
from utils import ft_request, to_json_file


def json_reply(dict_obj):
	json_obj = dumps(dict_obj["responsShips"], indent=4)
	print(json_obj)
	return loads(json_obj)


def reply_handler(message: dict):
	return json_reply(message)


if "__main__" == __name__:
	#input_coordinates = sys.argv[1]
	argp = argparse.ArgumentParser(description="Client for space scaning")
	argp.add_argument('coordinates', type=float, nargs=6, metavar="*", 
							help="use Equatorial coordinate system")
	args = argp.parse_args()

	to_json_file(ft_request(args.coordinates, reply_handler))
