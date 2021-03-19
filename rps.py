from random import randrange
import time

# Use unicode support in most terminals to boldify text
def print_bold(str):
	print("\033[1m" + str + "\033[0m")

class Game:

	score_pc = score_user = 0

	# Plays a single round: asks user for their move and generates a computer move
	def play_round(self):
		print("Press R for Rock, P for Paper or S for Scissors")
		s = input().casefold()

		if not self.validate_input(s):
			print(f"Invalid pick '{s}', try again")
			self.play_round()
		else:
			print("3...")
			time.sleep(1)
			print("2...")
			time.sleep(1)
			print("1...")
			time.sleep(1)
			self.handle_move(s, self.generate_pc_move(True))

	def validate_input(self, input):
		options = ["r", "p", "s"] 
		return input in options


	# Check whether the input moves are valid and determine winner based
	# on the usual rock, paper, scissors rules (rock beats scissors, scissors beats paper,
	# and paper beats rock)
	def handle_move(self, move_a, move_b):
		win_index = -1 # indicates invalid input move

		

		if move_a == "r":
			if move_b == "r":
				win_index = 2
			elif move_b == "p":
				win_index = 1
			elif move_b == "s":
				win_index = 0
		elif move_a == "p":
			if move_b == "r":
				win_index = 0
			elif move_b == "p":
				win_index = 2
			elif move_b == "s":
				win_index = 1
		elif move_a == "s":
			if move_b == "r":
				win_index = 1
			elif move_b == "p":
				win_index = 0
			elif move_b == "s":
				win_index = 2
		else:
			print(f"Unknown move {move_a}")
			

		self.process_move_result(win_index)

	# Check outcome, modify scores and write results to console
	def process_move_result(self, outcome):
		if outcome == 0:
			print_bold("You beat the computer!")
			self.score_user += 1
		elif outcome == 1:
			print_bold("Computer won this round.")
			self.score_pc += 1
		elif outcome == 2:
			print_bold("Tie!")
		else:
			print_bold("invalid")

		print(f"Score: You {self.score_user} - {self.score_pc} Computer")


	# Starts a new round or quits, printing the final score
	def start_game(self):
		print_bold("Press P to play or Q to quit")
		input_str = input().lower()
		
		if input_str == "p":
			self.play_round()
		elif input_str == "q":
			print(f"Final score: You {self.score_user} - {self.score_pc} Computer")
			exit()
		else:
			print(f"Unknown input '{input_str}'")
			self.start_game()

	# Randomly generate a pc move
	def generate_pc_move(self, print_move = True):
		move = ["r", "p", "s"][randrange(2)]
		if print_move:
			print(f"Computer picked {move.upper()}")
		return move

def main():
		print("Welcome to Rock Paper Scissors!")
		game = Game()
		while True:
			game.start_game()

if __name__ == "__main__":
		main()
