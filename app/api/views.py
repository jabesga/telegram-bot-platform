from app import app, socketio
from app.bot.models import Bot
from flask import request, jsonify, render_template
import json
from flask_socketio import emit

 
@app.route("/bot/<auth_token>/", methods=['GET'])
def bot_get(auth_token):
    new_bot = Bot(auth_token)
    response = new_bot.get_me()
    return jsonify(response)
        
@app.route("/bot/<auth_token>/updates/", methods=['GET', 'POST'])
def bot_get_updates(auth_token):
    if request.method == 'POST':
        new_bot = Bot(auth_token)
        response = new_bot.get_updates(request.json['offset'], request.json['limit'], request.json['timeout'])
        return str(response)
    else:
        new_bot = Bot(auth_token)
        response = new_bot.get_updates(request.args.get('offset', ''), request.args.get('limit', ''), request.args.get('timeout', ''))
        return jsonify(response)

@app.route("/bot/<auth_token>/webhook/add/", methods=['GET'])
def bot_add(auth_token):
    new_bot = Bot(auth_token)
    response = new_bot.set_webhook(app.DOMAIN + '/bot/' + auth_token + '/webhook/')
    return jsonify(response)

@app.route("/bot/<auth_token>/webhook/remove/", methods=['GET'])
def bot_remove(auth_token):
    new_bot = Bot(auth_token)
    response = new_bot.delete_webhook()
    return jsonify(response)
    
@app.route("/bot/<auth_token>/webhook/", methods=['GET', 'POST'])
def bot_webhook(auth_token):
    if request.method == 'POST':
        request.namespace = '/webhook'
        emit('webhook', {'data': request.data}, broadcast=True)
        print(request.data)
        return json.dumps(True)
    else:
        return render_template('bot_realtime_updates.html')
        
@app.route("/bot/<auth_token>/send/", methods=['GET', 'POST'])
def bot_send_message(auth_token):
    if request.method == 'POST':
        new_bot = Bot(auth_token)
        response = new_bot.send_message(request.json['channel'], request.json['text'], request.json['parse'])
        return str(response)
    else:
        new_bot = Bot(auth_token)
        response = new_bot.send_message(
            request.args.get('channel', ''), 
            request.args.get('text', ''),
            parse_mode=request.args.get('parse', ''),
            reply_to_message_id=request.args.get('reply',''))
            
        return jsonify(response)

@app.route("/bot/<auth_token>/forward/<chat_id>/<from_chat_id>/<message_id>/", methods=['GET', 'POST'])
def bot_forward_message(auth_token, chat_id, from_chat_id, message_id):
    if request.method == 'POST':
        new_bot = Bot(auth_token)
        response = new_bot.send_message(request.json['channel'], request.json['text'], request.json['parse'])
        return str(response)
    else:
        new_bot = Bot(auth_token)
        response = new_bot.forward_message(chat_id, from_chat_id, message_id)
        return jsonify(response)