import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

tictactoe_app = Flask(__name__, template_folder='../views', static_folder='../static')
tictactoe_app.config['SECRET_KEY'] = os.urandom(24)
tictactoe_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
tictactoe_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../game_scores.db'

db = SQLAlchemy(tictactoe_app)


