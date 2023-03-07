import game
from copycat import Copycat
from cheater import Cheater
from cooperator import Cooperator
from grudger import Grudger
from detective import Detective
from custom import CustomPlayer


class GameProcess:

	def __init__(self):
		self.game = game.Game()
		self.jugador = [
							Copycat(game.CC),
							Cheater(game.CH),
							Cooperator(game.CO),
							Grudger(game.GR),
							Detective(game.DT),
							CustomPlayer(game.CP) # Comment me for checking the default game
						]


	def printAllScores(self):
		print("\t-> copycat: ", self.jugador[0].candies)
		print("\t-> cheater: ", self.jugador[1].candies)
		print("\t-> cooperator: ", self.jugador[2].candies)
		print("\t-> grudger: ", self.jugador[3].candies)
		print("\t-> detective: ", self.jugador[4].candies)
		print("\t-> custom player: ", self.jugador[5].candies) # Comment me for checking the default game


	def everyoneWithEveryone(self):
		for i in range(len(self.jugador)):
			for j in range(i + 1, len(self.jugador)):
				print("\t/\/\/", self.jugador[i].name, "<--->", self.jugador[j].name, "/\/\/")
				self.game.play(self.jugador[i], self.jugador[j])
				print("GENERAL_RESULT:")
				self.printAllScores()
				print("TOP_3:")
				self.game.top3()
				print("_._._._._._._._._.", end="\n\n")
