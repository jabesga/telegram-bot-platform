from app import app
from app.bot.models import Bot
from flask import request, jsonify
import json

@app.route("/bot/<auth_token>/webhook/", methods=['POST'])
def bot_webhook(auth_token):
    if request.method == 'POST':
        print(request.data)
        return json.dumps(True)
    
@app.route("/bot/<auth_token>/add/", methods=['GET'])
def bot_add(auth_token):
    new_bot = Bot(auth_token)
    response = new_bot.set_webhook(app.DOMAIN + '/bot/webhook/' + auth_token)
    return jsonify(response)

@app.route("/bot/<auth_token>/remove/", methods=['GET'])
def bot_remove(auth_token):
    new_bot = Bot(auth_token)
    response = new_bot.delete_webhook()
    return jsonify(response)
    
@app.route("/bot/<auth_token>/", methods=['GET'])
def bot_get(auth_token):
    new_bot = Bot(auth_token)
    response = new_bot.get_me()
    return jsonify(response)

@app.route("/bot/<auth_token>/send/", methods=['GET', 'POST'])
def bot_send_message(auth_token):
    if request.method == 'POST':
        new_bot = Bot(auth_token)
        response = new_bot.send_message(request.json['channel'], request.json['text'], request.json['parse'])
        return str(response)
    else:
        new_bot = Bot(auth_token)
        response = new_bot.send_message(request.args.get('channel', ''), request.args.get('text', ''), request.args.get('parse', ''))
        return jsonify(response)
        
@app.route("/bot/<auth_token>/updates/", methods=['GET', 'POST'])
def bot_get_update(auth_token):
    if request.method == 'POST':
        new_bot = Bot(auth_token)
        response = new_bot.get_updates(request.json['offset'], request.json['limit'], request.json['timeout'])
        return str(response)
    else:
        new_bot = Bot(auth_token)
        response = new_bot.get_updates(request.args.get('offset', ''), request.args.get('limit', ''), request.args.get('timeout', ''))
        return jsonify(response)