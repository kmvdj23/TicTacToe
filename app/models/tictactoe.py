import json
class TicTacToe():

	def __init__(self):
		row1 = list('   ')
		row2 = list('   ')
		row3 = list('   ')
		self.board = list()
		self.board.append(row1)
		self.board.append(row2)
		self.board.append(row3)
		
		self.player1 = list('XXXXX')
		self.player2 = list('OOOO')
	
		self.moves = {
			'1' : (0,0),
			'2' : (0,1),
			'3' : (0,2),
			'4' : (1,0),
			'5' : (1,1),
			'6' : (1,2),
			'7' : (2,0),
			'8' : (2,1),
			'9' : (2,2),
		}

		self.turn = 1
		
	def place_move(self, position):
		
		position = str(position)
		if self.turn == 1:
			if self.check_coordinates(position):
				coordinates = self.moves[position]
				self.board[coordinates[0]][coordinates[1]] = self.player1.pop()
				self.turn = 2
				return
			self.turn = 1
			
		else:
			if self.check_coordinates(position):
				coordinates = self.moves[position]
				self.board[coordinates[0]][coordinates[1]] = self.player2.pop()
				self.turn = 1
				return
			self.turn = 2
			


	def check_coordinates(self, position):
		if int(position) > 9:
			return False
		coordinates = self.moves[position]
		if self.board[coordinates[0]][coordinates[1]] == ' ':
			return True
		return False

	def check_winner(self, player):
		for x in range(0,3):
			if ((self.board[x][0] == self.board[x][1]) and (self.board[x][1] == self.board[x][2]) and (self.board[x][2] != ' ')) or ((self.board[0][x] == self.board[1][x]) and (self.board[1][x] == self.board[2][x]) and (self.board[2][x] != ' ')):
				return 'Player {0} wins!'.format(player)
		if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[1][1] != ' ') or (self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[1][1] != ' ') :
			return 'Player {0} wins!'.format(player)
		elif not self.player1 and not self.player2:
			return 'DRAW' 
		return None

	@classmethod
	def to_dict(cls, obj):
		game = { 'board' : obj.board,
			'turn' : obj.turn,
			'player1' : obj.player1,
			'player2' : obj.player2
		}
		return game

	@classmethod
	def from_dict(cls, obj):
		game = TicTacToe()
		game.board = obj['board']
		game.player1 = obj['player1']
		game.player2 = obj['player2']
		game.turn = obj['turn']
		return game


if __name__ == '__main__':
	game = TicTacToe()