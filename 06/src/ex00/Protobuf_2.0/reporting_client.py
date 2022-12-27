# ~$ ./reporting_client.py 17 45 40.0409 −29 00 28.118
import sys
import grpc
from time import sleep
from json import dumps, loads
from spaceships_pb2 import SpaceshipRequest
from spaceships_pb2_grpc import SpaceshipsStub
from google.protobuf.json_format import MessageToJson, MessageToDict


def to_json_file(list_obj):
	with open("reply_data.json", 'w') as outfile:
		outfile.write(dumps(list_obj, indent=4))


def return_json_reply(dict_obj):
	json_obj = dumps(dict_obj["responsShips"], indent=4)
	print(json_obj)
	return loads(json_obj)


def ft_request(input_coordinates):
	# create connection channel
	with grpc.insecure_channel("localhost:8888") as channel:
		list_reply = []
		# set up connection on opening channel
		client = SpaceshipsStub(channel)
		# generate the request
		request = SpaceshipRequest(coordinates=input_coordinates)
		# send request to remote server
		replies = client.SendSpaceship(request)
		# receive ships from server
		for reply in replies:
			dict_obj = MessageToDict(reply)
			list_reply.append(return_json_reply(dict_obj))
			sleep(1)
		return list_reply


if "__main__" == __name__:
	input_coordinates = sys.argv[1]

	#print(sys.argv[1])
	#"""[Set to JSON]"""
	to_json_file(ft_request(input_coordinates))
