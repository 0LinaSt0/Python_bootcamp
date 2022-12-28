
import grpc, sys
from time import sleep
from json import dumps
from google.protobuf.json_format import MessageToDict
sys.path.insert(1, "./general_srcs/proto_srcs/")
from spaceships_pb2 import SpaceshipRequest
from spaceships_pb2_grpc import SpaceshipsStub


def to_json_file(list_obj):
	with open("reply_data.json", 'w') as outfile:
		outfile.write(dumps(list_obj, indent=4))


def ft_request(input_coordinates, ft_handler):
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
			appending_message = ft_handler(dict_obj)
			list_reply.append(appending_message)
		return list_reply
