import game
from player import Player


"""
Copycat gives COOP first time and just gives
another guy's last bet all next times
"""
class Copycat(Player):

	def doingBet(self):
		if self.opponent_last_bet == game.NUN:
			return game.COOP
		return self.opponent_last_bet
