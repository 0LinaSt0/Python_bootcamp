import pytest
import mock
import builtins
import sys
from conftest import (
	INCORRECTLY, 
	CORRECTLY,
	INPUT_FLAG
)
sys.path.insert(1, "../ex00")
from customException import customException


QUESTIONS_NUMBER = 10


def is_equivalent(capfd, reactions_obj, reaction, reaction_checker, 
					expected_result):
	reactions_obj.degree(reaction, reaction_checker)
	out, err = capfd.readouterr()
	assert out == expected_result


def test_for_respiration(capfd, reactions_obj):
	reaction = "respiration"
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "23"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_respiration, CORRECTLY)
	with mock.patch.object(builtins,INPUT_FLAG, lambda _: "2356"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_respiration, CORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: ""):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_respiration, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "fgsartg"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_respiration, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "-5"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_respiration, INCORRECTLY)

	
def test_for_heartRate(capfd, reactions_obj):
	reaction = "heart_rate"
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "45"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_heartRate, CORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "456"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_heartRate, CORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "-45"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_heartRate, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: ""):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_heartRate, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "zdfbz "):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_heartRate, INCORRECTLY)



def test_for_blushingLevel(capfd, reactions_obj):
	reaction = "blushing_level"
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "1"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_blushingLevel, CORRECTLY)
	with mock.patch.object(builtins,INPUT_FLAG, lambda _: "6"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_blushingLevel, CORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "-1"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_blushingLevel, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "7"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_blushingLevel, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: ""):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_blushingLevel, INCORRECTLY)
	with mock.patch.object(builtins,INPUT_FLAG, lambda _: "dvdaervb"):
		is_equivalent(capfd, reactions_obj, reaction,
						reactions_obj.check_blushingLevel, INCORRECTLY)


def test_for_pupillaryDilation(capfd, reactions_obj):
	reaction = "pupillary_dilation"
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "2"):
		is_equivalent(capfd, reactions_obj, reaction, 
						reactions_obj.check_pupillaryDilation, CORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "8"):
		is_equivalent(capfd, reactions_obj, reaction, 
						reactions_obj.check_pupillaryDilation, CORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "9"):
		is_equivalent(capfd, reactions_obj, reaction, 
						reactions_obj.check_pupillaryDilation, INCORRECTLY)
	with mock.patch.object(builtins,INPUT_FLAG, lambda _: "-2"):
		is_equivalent(capfd, reactions_obj, reaction, 
						reactions_obj.check_pupillaryDilation, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: " "):
		is_equivalent(capfd, reactions_obj, reaction, 
						reactions_obj.check_pupillaryDilation, INCORRECTLY)
	with mock.patch.object(builtins, INPUT_FLAG, lambda _: "weva"):
		is_equivalent(capfd, reactions_obj, reaction, 
						reactions_obj.check_pupillaryDilation, INCORRECTLY)


def exec_reaction(reac_obj, reac_coutn, reac_key, reac_func, questions_count,
					expected_result):
	reac_obj.reactions[reac_key] = reac_coutn
	assert reac_func(questions_count) == expected_result


def test_is_respiration_norm(reactions_obj):
	key = "respiration"
	exec_func = reactions_obj.is_respiration_norm
	exec_reaction(reactions_obj, 10, key, exec_func, QUESTIONS_NUMBER, -1)
	exec_reaction(reactions_obj, 20, key, exec_func, QUESTIONS_NUMBER, -1)
	exec_reaction(reactions_obj, 130, key, exec_func, QUESTIONS_NUMBER, 1)
	exec_reaction(reactions_obj, 160, key, exec_func, QUESTIONS_NUMBER, 1)
	try:
		exec_reaction(reactions_obj, 1, key, exec_func, 0, 1)
	except customException as e:
		assert e.args[0] == "\nError: something wrong [check Reaction.is_respiration_norm()]\n"


def test_is_heartRate_norm(reactions_obj):
	key = "heart_rate"
	exec_func = reactions_obj.is_heartRate_norm
	exec_reaction(reactions_obj, 10, key, exec_func, QUESTIONS_NUMBER, -1)
	exec_reaction(reactions_obj, 123, key, exec_func, QUESTIONS_NUMBER, -1)
	exec_reaction(reactions_obj, 650, key, exec_func, QUESTIONS_NUMBER, 1)
	exec_reaction(reactions_obj, 1000, key, exec_func, QUESTIONS_NUMBER, 1)
	try:
		exec_reaction(reactions_obj, 1, key, exec_func, 0, 1)
	except customException as e:
		assert e.args[0] == "\nError: something wrong [check Reaction.is_heartRate_norm()]\n"


def test_is_blushingLevel_norm(reactions_obj):
	key = "blushing_level"
	exec_func = reactions_obj.is_blushingLevel_norm
	exec_reaction(reactions_obj, 100, key, exec_func, QUESTIONS_NUMBER, 1)
	exec_reaction(reactions_obj, 1245, key, exec_func, QUESTIONS_NUMBER, 1)
	exec_reaction(reactions_obj, 10, key, exec_func, QUESTIONS_NUMBER, -1)
	exec_reaction(reactions_obj, 26, key, exec_func, QUESTIONS_NUMBER, -1)
	try:
		exec_reaction(reactions_obj, 1, key, exec_func, 0, 1)
	except customException as e:
		assert e.args[0] == "\nError: something wrong [check Reaction.is_blushingLevel_norm()]\n"


def test_is_pupillaryDilation_norm(reactions_obj):
	key = "pupillary_dilation"
	exec_func = reactions_obj.is_pupillaryDilation_norm
	exec_reaction(reactions_obj, 140, key, exec_func, QUESTIONS_NUMBER, 1)
	exec_reaction(reactions_obj, 145, key, exec_func, QUESTIONS_NUMBER, 1)
	exec_reaction(reactions_obj, 20, key, exec_func, QUESTIONS_NUMBER, -1)
	exec_reaction(reactions_obj, 49, key, exec_func, QUESTIONS_NUMBER, -1)
	try:
		exec_reaction(reactions_obj, 1, key, exec_func, 0, 1)
	except customException as e:
		assert e.args[0] == "\nError: something wrong [check Reaction.is_pupillaryDilation_norm()]\n"
