import game
from player import Player


"""
It plays as Copycat but if another guy's bet is COOP
6 times, CustomPlayer CHEATs every time late
"""
class CustomPlayer(Player):

	def doingBet(self):
		if self.opponent_last_bet == game.NUN:
			return game.COOP
		if self.opponent_last_bet == game.COOP:
			self.coop_iter += 1
		if self.coop_iter > 6:
			return game.CHEAT
		return self.opponent_last_bet
