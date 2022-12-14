# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/30 19:58:00 by msalena           #+#    #+#              #
#    Updated: 2022/12/01 15:20:08 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import Counter

nun, coop, cheat = range(3)
cp = "copycat"
ch = "cheater"
co = "cooperator"
gr = "grudger"
dt = "detective"

class Game(object):

	def __init__(self, matches=10):
		self.matches = matches
		self.registry = Counter()

	def play(self, player1, player2):
		self.registry.update({cp: 0, ch: 0, co: 0, gr: 0, dt: 0})
		for i in range(self.matches):
			bet_p1 = player1.doingBet()
			bet_p2 = player2.doingBet()
			player1.opponentLastBet(bet_p2)
			player2.opponentLastBet(bet_p1)
			if bet_p1 == coop and bet_p2 == coop:
				self.registry[player1.name] += 2
				self.registry[player2.name] += 2
			elif bet_p1 == coop and bet_p2 == cheat:
				self.registry[player1.name] -= 1
				self.registry[player2.name] += 3
			elif bet_p1 == cheat and bet_p2 == coop:
				self.registry[player1.name] += 3
				self.registry[player2.name] -= 1
		player1.updateInformation(self.registry[player1.name])
		player2.updateInformation(self.registry[player2.name])

	def top3(self):
		data = self.registry.most_common()
		for i in range(3):
			print(data[i][0], data[i][1])
