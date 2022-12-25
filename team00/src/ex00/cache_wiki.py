from urllib import parse, request
import argparse
import json
import html_to_json
from collections import Counter

START_URL_NAME = "42_(school)"
JSON_FILE_NAME = "wiki.json"

def take_input_url():
	iput_parser = argparse.ArgumentParser(description="Article_name")
	iput_parser.add_argument('-p', dest="p", type=str)
	arg =  iput_parser.parse_args()
	START_URL_NAME = parse.quote(arg.p.replace(' ', '_'))
	url = 'https://en.wikipedia.org/wiki/{}'.format(START_URL_NAME)
	print(url)
	return url


def	read_url_page(url):
	response = request.urlopen(url)
	data = response.read().decode("utf-8")
	with open(JSON_FILE_NAME, "w") as file:
		file.write(json.dumps(html_to_json.convert(data), indent=4))

def url_count(json_dict):
	url_iterator = (filter(lambda x: x.startswith("/wiki/"), json_dict[elem]) for elem in json_dict)
	counter = [Counter(v) for v in url_iterator]
	print(counter)

if "__main__" == __name__:
	read_url_page(take_input_url())
	with open(JSON_FILE_NAME) as opened_json:
		json_dict = json.load(opened_json)
		print(type(json_dict))
		url_count(json_dict)