
GOLD_KEY = "gold_ingots"

def empty(purse):
	r_purse = purse.copy()
	r_purse.clear()
	return r_purse

def add_ingot(purse):
	r_purse = purse.copy()
	(r_purse.update({GOLD_KEY: r_purse[GOLD_KEY] + 1}) if GOLD_KEY in r_purse
		else r_purse.update({GOLD_KEY: 1}))
	return r_purse

def get_ingot(purse):
	r_purse = purse.copy()
	if GOLD_KEY in r_purse and r_purse[GOLD_KEY] != 0:
		r_purse.update({GOLD_KEY: r_purse[GOLD_KEY] - 1})
	return r_purse

