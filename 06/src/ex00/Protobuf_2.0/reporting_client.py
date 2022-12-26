# ~$ ./reporting_client.py 17 45 40.0409 −29 00 28.118
import sys
import grpc
from spaceships_pb2 import SpaceshipRequest
from spaceships_pb2_grpc import SpaceshipsStub

def ft_request(input_coordinates):
	# create connection channel
	with grpc.insecure_channel("localhost:8888") as channel:
		# set up connection on opening channel
		client = SpaceshipsStub(channel)
		print(input_coordinates)
		# generate the request
		request = SpaceshipRequest(coordinates=input_coordinates)
		# send request to remote server
		reply = client.SendSpaceship(request)
		print(reply)

if "__main__" == __name__:
	input_coordinates = sys.argv[1]

	print(sys.argv[1])
	#"""[Set to JSON]"""
	ft_request(input_coordinates)
