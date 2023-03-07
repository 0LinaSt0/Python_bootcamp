from pytest import fixture


@fixture
def subject_first_result():
	return [
		"plug cable1 into socket1 using plug1",
		"plug cable2 into socket2 using plug2",
		"plug cable3 into socket3 using plug3",
		"weld cable4 to socket4 without plug"
	]

@fixture
def subject_second_result():
	return [
		"plug cable2 into socket1 using plugZ",
		"plug cable1 into socket2 using plugY"
	]


@fixture
def empty_plugs_result():
	return [
		"weld cable2 to socket1 without plug",
		"weld cable1 to socket2 without plug"
	]


@fixture
def empty_cables_result():
	return []


@fixture
def one_socket_result():
	return ["weld cable2 to socket1 without plug"]
