#! /usr/bin/env python3

"""
{
	"alignment": "ally",
	"name": "Normandy",
	"class": "Corvette",
	"length": 216.3,
	"crew_size": 8,
	"armed": true,
	"officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
}
"""

from concurrent import futures # for creating tread pool

import grpc, sys
from spaceships_factory import ship_factory
sys.path.insert(1, "proto_srcs/")
import spaceships_pb2_grpc
from spaceships_pb2 import SpaceshipResponse



class SendSpaceshipService(
	spaceships_pb2_grpc.SpaceshipsServicer
):
	# as Spaceships service in proto (redefinition)
	def SendSpaceship(self, request, context):
		print(request)
		for _ in range(10):
			reply = SpaceshipResponse()
			reply.respons_ships.CopyFrom(ship_factory())
			yield reply



def server():
	# create gRPC server which using 10 threads
	serv = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	# associates above class with server
	spaceships_pb2_grpc.add_SpaceshipsServicer_to_server(
		SendSpaceshipService(), serv
	)
	# start server on 8888 port
	serv.add_insecure_port("localhost:8888")
	serv.start()
	# wait until stopped [^ctrl + C]
	serv.wait_for_termination()


if "__main__" == __name__:
	server()
