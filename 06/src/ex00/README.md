1. Install venv:
	$ python -m pip install virtualenv
	$ virtualenv venv

2. Activate venv:
	$ source venv/bin/activate OR . venv/bin/activate

3. Install gRPC and gRPC-tools:
	(venv) $ python -m pip install grpcio
	(venv) $ python -m pip install grpcio-tools

4. Install requiements:
	(venv) $ pip3 install -r requirements.txt

5. Generate protobufs:
	$ python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/spaceships.proto

