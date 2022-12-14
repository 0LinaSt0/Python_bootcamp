# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    players.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/30 19:57:58 by msalena           #+#    #+#              #
#    Updated: 2022/12/01 15:23:06 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import game

class Player(object):

	def __init__(self, name):
		self.name = name
		self.candies = 0
		self.opponent_bet = game.nun
		self.cheat_flag = False
		self.bet = game.coop
		self.start_iter = 0

	def returnDefaultValues(self):
		self.opponent_bet = game.nun
		self.cheat_flag = False
		self.bet = game.coop
		self.start_iter = 0

	def opponentLastBet(self, opponent_last_bet):
		self.opponent_bet = opponent_last_bet

	def updateInformation(self, game_result):
		self.candies = game_result
		self.returnDefaultValues()

class Cheater(Player):

	def doingBet(self):
		return game.cheat

class Cooperator(Player):

	def doingBet(self):
		return game.coop

class Copycat(Player):

	def doingBet(self):
		if self.opponent_bet == game.nun:
			return game.coop
		return self.opponent_bet

class Grudger(Player):

	def doingBet(self):
		if (self.cheat_flag == False
				and self.opponent_bet == game.cheat):
			self.bet = game.cheat
			self.cheat_flag = True
		return self.bet

class Detective(Player):

	start_cmds = [game.coop, game.cheat, game.coop, game.coop]

	def doingBet(self):
		if self.start_iter < 4:
			if (self.cheat_flag == False
					and self.opponent_bet == game.cheat):
				self.cheat_flag = True
			self.start_iter += 1
			return self.start_cmds[self.start_iter - 1]
		if self.cheat_flag == True:
			return self.opponent_bet
		return game.cheat
