## Preparing steps
#### 1. Install venv:
	$ python -m pip install virtualenv
	$ virtualenv venv

#### 2. Activate venv:
	$ source venv/bin/activate OR . venv/bin/activate

#### 3. Install requiements:
	$ pip3 install -r requirements.txt

---
## EXERCISES

#### EX00 information:
Command for generating protobuf classes (from folder Protobuf_2.0/):
```shell
$ python -m grpc_tools.protoc -I ../src_proto --python_out=. --pyi_out=. --grpc_python_out=. ../src_proto/spaceships.proto
```

###### 1. Start server in folder "Protobuf_2.0/":
	```shell
	$ python3 reporting_server.py
	```
###### 2. Start client with coordinates (example: 17 45 40.0409 −29 00 28.118) in folder "Protobuf_2.0/":
	```shell
	python reporting_client.py <COORDINATES>
	```


