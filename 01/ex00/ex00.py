"""
MappingProxyType is immutable dict tipe:
https://adamj.eu/tech/2022/01/05/how-to-make-immutable-dict-in-python/
"""


from types import MappingProxyType


GOLD_KEY = "gold_ingots"


# return empty purse
def empty(purse):
	r_purse = MappingProxyType({})
	return r_purse


#copy coming purse, add gold ingot to it and return this copy
def add_ingot(purse):
	r_purse = purse.copy()
	(r_purse.update({GOLD_KEY: r_purse[GOLD_KEY] + 1}) if GOLD_KEY in r_purse
		else r_purse.update({GOLD_KEY: 1}))
	return MappingProxyType(r_purse)


#copy coming purse, get gold ingot from it (if gold exists) and return this copy
def get_ingot(purse):
	r_purse = purse.copy()
	if GOLD_KEY in r_purse and r_purse[GOLD_KEY] != 0:
		r_purse.update({GOLD_KEY: r_purse[GOLD_KEY] - 1})
	return MappingProxyType(r_purse)

