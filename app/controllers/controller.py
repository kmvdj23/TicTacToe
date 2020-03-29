from app.config import tictactoe_app, db
from app.models import TicTacToe, Result
from flask import render_template, redirect, url_for, request, session

@tictactoe_app.route('/')
def start_page():
	return render_template('index.html')

@tictactoe_app.route('/game', methods=['POST'])
def game_page():
	if request.method == 'POST': 
		player1 = request.form.get('player1')
		player2 = request.form.get('player2')
		game = TicTacToe()
		session['game'] = TicTacToe.to_dict(game) 
		session['player1'] = player1
		session['player2'] = player2
		return render_template('game.html')
	else:
		return redirect(url_for('start_page'))


@tictactoe_app.route('/place_move', methods=['POST'])
def add_move():
	if request.method == 'POST':
		move = request.form.get('move')
		game = TicTacToe.from_dict(session['game'])
		game.place_move(move)
		if game.turn == 1:
			winner = game.check_winner(session['player2'])
			if winner and winner != 'DRAW':
				add_results(session['player2'], session['player1'])
				return render_template('game.html', winner=winner)
			elif winner == 'DRAW':
				add_players(session['player2'], session['player1'])
				return render_template('game.html', winner=winner)
		else:
			winner = game.check_winner(session['player1'])
			if winner and winner != 'DRAW':
				add_results(session['player1'], session['player2'])
				return render_template('game.html', winner=winner)
			elif winner == 'DRAW':
				add_players(session['player2'], session['player1'])
				return render_template('game.html', winner=winner)
		session['game'] = TicTacToe.to_dict(game)
		return render_template('game.html')

@tictactoe_app.route('/game_results', methods=['GET'])
def show_results():
	results = Result.query.order_by(db.desc(Result.score)).all()
	return render_template('results.html', results=results)

def add_results(winner_name,loser_name):
	winner = Result.find_player(winner_name)
	if winner:
		winner.score += 1
	else:
		winner = Result(player_name=winner_name,score=1)
		db.session.add(winner)
	loser = Result.find_player(loser_name)
	if not loser:
		loser = Result(player_name=loser_name,score=0)
		db.session.add(loser)
	db.session.commit()

def add_players(player1_name,player2_name):
	player1 = Result.find_player(player1_name)
	if not player1:
		player1 = Result(player_name=player1_name,score=1)
		db.session.add(player1)
	player2 = Result.find_player(player2_name)
	if not player2:
		player2 = Result(player_name=player2_name,score=0)
		db.session.add(player2)
	db.session.commit()

