import game
from player import Player


"""
Cooperator alwayse gives COOP
"""
class Cooperator(Player):

	def doingBet(self):
		return game.COOP
