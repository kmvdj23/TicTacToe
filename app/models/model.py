from app.models.tictactoe import TicTacToe
from app.config import db

class Result(db.Model):

	__tablename__ = 'result'

	id = db.Column(db.Integer, primary_key=True)
	player_name = db.Column(db.String(30), nullable=False)
	score = db.Column(db.Integer, nullable=False)

	@classmethod
	def find_player(cls, player_name):
		return Result.query.filter(cls.player_name == player_name).first()