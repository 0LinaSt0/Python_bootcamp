from collections import Counter

NUN, COOP, CHEAT = range(3)
CC = "copycat"
CH = "cheater"
CO = "cooperator"
GR = "grudger"
DT = "detective"
CP = "CustomPlayer"


class Game(object):

	tournire_table = {CC: 0, CH: 0, CO: 0, GR: 0, DT: 0, CP: 0}

	def __init__(self, matches=10):
		self.matches = matches
		self.registry = Counter(self.tournire_table)

	def play(self, player1, player2):
		for i in range(self.matches):
			bet_p1 = player1.doingBet()
			bet_p2 = player2.doingBet()
			player1.opponentLastBet(bet_p2)
			player2.opponentLastBet(bet_p1)
			if bet_p1 == COOP and bet_p2 == COOP:
				self.registry[player1.name] += 2
				self.registry[player2.name] += 2
			elif bet_p1 == COOP and bet_p2 == CHEAT:
				self.registry[player1.name] -= 1
				self.registry[player2.name] += 3
			elif bet_p1 == CHEAT and bet_p2 == COOP:
				self.registry[player1.name] += 3
				self.registry[player2.name] -= 1
		player1.updateInformation(self.registry[player1.name])
		player2.updateInformation(self.registry[player2.name])

	def top3(self):
		standing = self.registry.most_common()
		for i in range(3):
			print("\t {}. {}: {}".format((i + 1), standing[i][0], standing[i][1]))
