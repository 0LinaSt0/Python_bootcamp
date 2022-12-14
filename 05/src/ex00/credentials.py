"""
envirion -

RESPONSE_INFO = "credentials": ...
"""

# for creating server for testing
from wsgiref.simple_server import make_server
# for wsgi implementation
from cgi import parse_qs, escape

FOUND_STATUS = "200 STATUS"
UNKNOWN_STATUS = "404 STATUS"
SPECIES_LIST = {
	"Cyberman": "John Lumic",
	"Dalek": "Davros",
	"Judoon": "Shadow Proclamation Convention 15 Enforcer",
	"Human": "Leonardo da Vinci",
	"Ood": "Klineman Halpen",
	"Silence": "Tasha Lem",
	"Slitheen": "Coca-Cola salesman",
	"Sontaran": "General Staal",
	"Time Lord": "Rassilon",
	"Weeping Angel": "The Division Representative",
	"Zygon": "Broton"
}

def my_WSGI(environ, start_response):
	# Returns a dictionary in which the values are lists
	cURL = parse_qs(environ['QUERY_STRING'])

	# Gets name of leadership from cURL
	leadership = cURL.get('species')[0] # Returns the first species value

	is_species_in_list = True if leadership in SPECIES_LIST else False

	response_body = (
		"{\"credentials\": \"" + ((SPECIES_LIST[leadership] if is_species_in_list is True else "Unknown")) + "\"}"
	)

	status = (FOUND_STATUS if is_species_in_list is True
				else UNKNOWN_STATUS)

	response_headers = [
		('Content-Type', 'text'), # MIME content type of the output stream
		('Content-Length', str(len(response_body))) # length (in bytes) of the output stream
	]

	start_response(status, response_headers)
	return [response_body.encode()]


if "__main__" == __name__:
	http = make_server("127.0.0.1", 8888, my_WSGI)
	# server will quit after single request
	#http.handle_request()
	# server will be running forever (ctrl+C can interrupt it)
	http.serve_forever()
