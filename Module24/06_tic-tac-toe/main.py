from Tictactoe import Board
from Tictactoe import Player
from Tictactoe import Game

my_board = Board()
f_player = Player('Ivan', 'X')
s_player = Player('Alex', 'O')
new_game = Game(True, f_player, s_player, my_board)

new_game.run_game()
# print(len(new_game.wall_of_fame))
