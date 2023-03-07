import sys
import logging
import requests as requests
from pathlib import Path

my_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=my_format, level=logging.INFO, datefmt="%H:%M:%S")
logger = logging.getLogger("my_logger")

URL = "http://127.0.0.1:8888/upload/"

def usage():
	print("""
% python screwdriver.py upload /path/to/file.mp3 
should upload the local audio file /path/to/file.mp3 
to the server

% python screwdriver.py list should retrieve and print 
out the names of all the files currently present on the server.
	""")


def get_list():
	res = requests.get(URL)
	if 200 == res.status_code:
		try:
			res = res.json()
			return res.get("audios", [])
		except Exception as error:
			print(error)
	else:
		print("ERROR: status code {}".format(res.status_code))
	return []



def upload_file(file_path):
	with open(file_path, "rb") as f:
		res = requests.post(URL, files=dict
		(inputFile=(Path(file_path).name, f.read()))
		)


if "__main__" == __name__:
	argv_count = len(sys.argv)
	if argv_count == 2 and sys.argv[1] == "list":
		[print(elem) for elem in get_list()]
	elif argv_count == 3 and sys.argv[1] == "upload":
		upload_file(sys.argv[2])
	else:
		usage()

