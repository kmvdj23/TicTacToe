from app.controllers import tictactoe_app

if __name__ == '__main__':
	tictactoe_app.run('localhost', port=80, debug=True)