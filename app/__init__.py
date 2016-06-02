from flask import Flask

app = Flask(__name__)
app.DOMAIN = 'https://telegrambot-pyframework-jabesga.c9users.io'

import core.views
import api.views