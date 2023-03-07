import game
from player import Player


"""
Cheater alwayse gives CHEAT
"""
class Cheater(Player):

	def doingBet(self):
		return game.CHEAT
