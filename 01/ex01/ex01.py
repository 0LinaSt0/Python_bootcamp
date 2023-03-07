from types import MappingProxyType


GOLD_KEY = "gold_ingots"


def all_gold(*purses):
	gold_count = 0
	for purse in purses:
		if GOLD_KEY in purse:
			gold_count += purse[GOLD_KEY]
	return gold_count


def gold_for_every_gentlemen(gold_count):
	equally_gold = gold_count // 3
	remainder = gold_count - (equally_gold * 3)
	gold_parts = [int(equally_gold), int(equally_gold), int(equally_gold)]
	i = 0

	while remainder:
		gold_parts[i] += 1
		remainder -= 1
		i += 1
		if i > 2:
			i = 0
	return gold_parts

def result_booty(gentls_gold):
	p0 = {GOLD_KEY: gentls_gold[0]}
	p1 = {GOLD_KEY: gentls_gold[1]}
	p2 = {GOLD_KEY: gentls_gold[2]}
	return MappingProxyType(p0), MappingProxyType(p1), MappingProxyType(p2)

def split_booty(*purses):
	booty = all_gold(*purses)
	return result_booty(gold_for_every_gentlemen(booty))

