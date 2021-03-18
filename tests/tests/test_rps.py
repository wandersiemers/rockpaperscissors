from rps import Game
import pytest

class TestGame():

	def test_start_game(self, capfd, game, monkeypatch):
		monkeypatch.setattr('builtins.input', lambda: 'p')
		game.start_game()

		out, err = capfd.readouterr()
		assert "Press R for Rock, P for Paper or S for Scissors" in out

	def test_handle_winning_move(self, capfd, game):
		winning_combinations = [("p", "r"), ("s", "p"), ("s", "p")]

		for combination in winning_combinations:
			game.handle_move(combination[0], combination[1])
			out, err = capfd.readouterr()
			assert "You beat the computer!" in out
			assert "Computer won this round." not in out

	def test_handle_losing_move(self, capfd, game):
		losing_combinations = [("r", "p"), ("p", "s"), ("p", "s")]

		for combination in losing_combinations:
			game.handle_move(combination[0], combination[1])
			out, err = capfd.readouterr()
			assert "Computer won this round." in out
			assert "You beat the computer!" not in out
	