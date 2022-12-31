import pytest
import mock
import builtins
import json

INCORRECTLY = "!INCORRECTLY!\n"
CORRECTLY = "CORRECTLY\n"


def is_equivalent(capfd, answers_obj, expected_result):
	answers_obj.append_answer(0)
	out, err = capfd.readouterr()
	assert out == expected_result


def test_not_int_answers(capfd, answers_obj):
	with mock.patch.object(builtins, "input", lambda _: "-1jfw"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "k"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: ""):
		is_equivalent(capfd, answers_obj, INCORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "\n"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)


def test_invalid_answers(capfd, answers_obj):
	with mock.patch.object(builtins, "input", lambda _: "0"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "4"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "123456"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "-6"):
		is_equivalent(capfd, answers_obj, INCORRECTLY)


def test_valid_answers(capfd, answers_obj):
	with mock.patch.object(builtins, "input", lambda _: "1"):
		is_equivalent(capfd, answers_obj, CORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "2"):
		is_equivalent(capfd, answers_obj, CORRECTLY)
	with mock.patch.object(builtins, "input", lambda _: "3"):
		is_equivalent(capfd, answers_obj, CORRECTLY)


def test_write_answers(answers_obj):
	# testing empty dicts
	returned_dict = {}
	assert answers_obj.write_answers() == json.dumps(returned_dict, indent=4)

	# testing added answers
	for i in range (1, 11):
		returned_dict[i] = i
		answers_obj.answers[i] = i
		assert answers_obj.write_answers() == json.dumps(returned_dict, indent=4)


def test_replicant_detector(answers_obj, answers_replicant_scenario, answer_human_scenario):
	# testing empty dict
	assert answers_obj.is_human() == 1

	#testing replicant scenario
	for key in answers_replicant_scenario:
		answers_obj.answers[key] = answers_replicant_scenario[key]
	assert answers_obj.is_human() == -1
	
	#testing human scenario
	answers_obj.answers = answer_human_scenario
	assert answers_obj.is_human() == 1
