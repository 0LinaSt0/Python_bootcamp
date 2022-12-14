from ex00 import *

"""TESTS_CODE"""
if __name__ == "__main__":
	def test00(purse):
		d0 = empty(purse)
		print("Empty: ", d0)
		d1 = add_ingot(d0)
		print(" Add: ", d1)
		d2 = get_ingot(d1)
		print("  Get: ", d2)
		d3 = add_ingot(d2)
		print("   Add: ", d3)
		print("   SUBJ_RESULT: ", add_ingot(get_ingot(add_ingot(empty(purse)))))

	def test01(purse):
		d0 = get_ingot(purse)
		print("Get: ", d0)
		d1 = get_ingot(d0)
		print(" Get:", d1)
		d2 = get_ingot(d1)
		print("  Get:", d2)
		d3 = empty(d2)
		print("   Empty:", d3)
		d4 = get_ingot(d3)
		print("    Get:", d4)
		d5 = add_ingot(d4)
		print("     Add:", d5)

	def test02(purse):
		d0 = add_ingot(purse)
		print("Add: ", d0)
		d1 = add_ingot(d0)
		print(" Add: ", d1)
		d2 = add_ingot(d1)
		print("  Add: ", d2)
		d3 = empty(d2)
		print("   Empty: ", d3)

	purse = {"gold_ingots": 2}
	print("\nINITIAL_PURSE: ", purse)
	print("\n\t~~TEST00(default)~~")
	test00(purse)
	print("\n\t~~TEST01(get_from_zero)~~")
	test01(purse)
	print("\n\t~~TEST02(add_emty_test)~~")
	test02(purse)
