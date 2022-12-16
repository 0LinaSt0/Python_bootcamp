import game


"""
Parent class for players
"""
class Player(object):

	def __init__(self, name):
		self.name = name
		self.candies = 0
		self.opponent_last_bet = game.NUN
		self.cheat_flag = False
		self.bet = game.COOP
		self.iter = 0
		self.coop_iter = 0


	def returnDefaultValues(self):
		self.opponent_last_bet = game.NUN
		self.cheat_flag = False
		self.bet = game.COOP
		self.iter = 0
		self.coop_iter = 0


	def opponentLastBet(self, opponent_last_bet):
		self.opponent_last_bet = opponent_last_bet


	def updateInformation(self, game_result):
		self.candies = game_result
		self.returnDefaultValues()
