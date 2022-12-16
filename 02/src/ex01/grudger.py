import game
from player import Player
from cheater import Cheater


"""
Grudger give COOP all time. But if another guy gave CHEAT once,
Grudger will be CHEATing all the time later
"""
class Grudger(Player):

	def doingBet(self):
		if (self.cheat_flag == False
				and self.opponent_last_bet == game.CHEAT):
			self.bet = Cheater.doingBet(self)
			self.cheat_flag = True
		return self.bet
