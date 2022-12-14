from ex02 import *


"""TESTS_CODE"""

def test00(purse):
	print("Add: ", end ='')
	d0 = add_ingot(purse)
	print("      ", d0)
	print("Get: ", end ='')
	d1 = get_ingot(d0)
	print("      ", d1)
	print("Add: ", end ='')
	d2 = add_ingot(d1)
	print("      ", d2)
	print("Empty: ", end ='')
	d3 = empty(d2)
	print("      ", d3)


if __name__ == "__main__":
	purse = {"gold_ingots": 5}
	print("\nINITIAL_PURSE: ", purse)
	print("\n\t~~TEST00(all_functs)~~")
	test00(purse)
