"""
{
	"alignment": "Ally",
	"name": "Normandy",
	"class": "Corvette",
	"length": 216.3,
	"crew_size": 8,
	"armed": true,
	"officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
}
"""

from concurrent import futures # for creating tread pool
import random

import grpc
import spaceships_pb2_grpc
from spaceships_pb2 import SpaceshipRequest, SpaceshipResponse

from spaceships_generator import ship_generator


class SendSpaceshipService(
	spaceships_pb2_grpc.SpaceshipsServicer
):
	# as Spaceships service in proto
	def SendSpaceship(self, request, context):
		sent_spaceships = [
			ship_generator()
			for _ in random(1, 10)
		]
		return SpaceshipResponse(respons_ship=sent_spaceships)



def server():
	# create gRPC server which using 10 threads
	serv = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	# associates above class with server
	spaceships_pb2_grpc.add_SpaceshipsServicer_to_server(
		SendSpaceshipService(), serv
	)
	# start server on 8888 port
	serv.add_insecure_port("[::]:8888")
	serv.start()
	# wait until stopped [^ctrl + C]
	serv.wait_for_termination()


if "__main__" == __name__:
	server()
