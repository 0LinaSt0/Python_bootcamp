import game
import players

class StartGame:

	def __init__(self):
		self.game = game.Game()
		self.jugadores = [players.Copycat(game.cp),
						players.Cheater(game.ch),
						players.Cooperator(game.co),
						players.Grudger(game.gr),
						players.Detective(game.dt)]

	def printAllScores(self):
		print("copycat: ", self.jugadores[0].candies, end=" -> ")
		print("cheater: ", self.jugadores[1].candies, end=" -> ")
		print("cooperator: ", self.jugadores[2].candies, end=" -> ")
		print("grudger: ", self.jugadores[3].candies, end=" -> ")
		print("detective: ", self.jugadores[4].candies)

	def everyoneWithEveryone(self):
		for i in range(len(self.jugadores)):
			for j in range(i + 1, len(self.jugadores)):
				print("\t/////", self.jugadores[i].name, "---", self.jugadores[j].name, "/////")
				self.game.play(self.jugadores[i], self.jugadores[j])
				print("+ General_result:")
				self.printAllScores()
				print("+ TOP_3:")
				self.game.top3()
				print("_._._._._._._._._.", end="\n\n")


start = StartGame()
start.everyoneWithEveryone()
