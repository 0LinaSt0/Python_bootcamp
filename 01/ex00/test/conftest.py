import pytest


@pytest.fixture
def purse_empty():
	return {}


@pytest.fixture
def purse_just_gold():
	return {"gold_ingots": 3}


@pytest.fixture
def purse_not_just_gold():
	return {"gold_ingots": 56, "rocks": 5, "buttons": 4}


@pytest.fixture
def purse_zero_gold():
	return {"gold_ingots": 0}


@pytest.fixture
def purse_without_gold():
	return {"rocks": 2, "buttons": 0, "paperclips": 10}
