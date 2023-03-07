#! /usr/bin/env python3

# ~$ ./reporting_client.py 17 45 40.0409 -29 00 28.118

import sys
from json import loads, dumps
sys.path.insert(1, "./general_srcs/")
from utils import ft_argparser, ft_request, to_json_file


def json_reply(dict_obj):
	json_obj = dumps(dict_obj["respons_ships"], indent=4)
	print(json_obj)
	return loads(json_obj)


def reply_handler(message: dict):
	return json_reply(message)


if "__main__" == __name__:
	to_json_file(ft_request(ft_argparser(), reply_handler))
