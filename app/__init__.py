from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_folder='static/')
app.DOMAIN = 'https://telegrambot-pyframework-jabesga.c9users.io'
socketio = SocketIO(app)

from .core import views
from .api import views