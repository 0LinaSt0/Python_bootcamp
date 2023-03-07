import pytest

@pytest.fixture
def some_purses_with_gold():
	return {'gold_ingots': 3}, {'gold_ingots': 2}, {'apples': 10}, {'cnopochki':8}


@pytest.fixture
def some_purses_without_gold():
	return {'pies': 3}, {'birds': 2}, {'apples': 10}


@pytest.fixture
def some_purses_with_one_gold():
	return {'pies': 3, 'gold_ingots': 1}, {'birds': 2}, {'apples': 10}


@pytest.fixture
def some_purses_with_two_gold():
	return {'gold_ingots': 2}, {'birds': 2}, {'apples': 10}


@pytest.fixture
def one_purse_with_gold():
	return {'gold_ingots': 565}
