from ex01 import *


"""TESTS_CODE"""

def test00():
	print("inpt: ", {"gold_ingots":3}, {"gold_ingots":2}, {"apples":10})
	print("outp: ", *split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}))

def test01():
	print("inpt: ", {"pies":3}, {"birds":2}, {"apples":10})
	print("outp: ", *split_booty({"pies":3}, {"birds":2}, {"apples":10}))

def test02():
	print("inpt: ", {"pies":3, "gold_ingots":1}, {"birds":2}, {"apples":10})
	print("outp: ", *split_booty({"pies":3, "gold_ingots":1}, {"birds":2}, {"apples":10}))

def test03():
	print("inpt: ", {"gold_ingots":0}, {"gold_ingots":0})
	print("outp: ", *split_booty({"gold_ingots":0}, {"gold_ingots":0}))

def test04():
	print("inpt: ", {"gold_ingots":565})
	print("outp: ", *split_booty({"gold_ingots":565}))

if __name__ == "__main__":
	print("\t~~TEST00(default)~~")
	test00()
	print("\n\t~~TEST01(without_gold)~~")
	test01()
	print("\n\t~~TEST02(just_one_gold)~~")
	test02()
	print("\n\t~~TEST03(zero_gold)~~")
	test03()
	print("\n\t~~TEST04(many_gold)~~")
	test04()
