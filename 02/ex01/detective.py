import game
from player import Player
from copycat import Copycat
from cheater import Cheater


"""
Detective playes [COOP, CHEAT, COOP, COOP] first 4 times.
If another guy gave him CHEAT just once, Detective switches into a Copycat.
Other way, Detective switches into a Cheater
"""
class Detective(Player):

	start_cmds = [game.COOP, game.CHEAT, game.COOP, game.COOP]


	def doingBet(self):
		if self.iter < 4:
			if (self.cheat_flag == False
					and self.opponent_last_bet == game.CHEAT):
				self.cheat_flag = True
			self.iter += 1
			return self.start_cmds[self.iter - 1]
		if self.cheat_flag == True:
			return Copycat.doingBet(self)
		return Cheater.doingBet(self)
