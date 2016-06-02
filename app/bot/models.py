import requests

class Bot():
    
    token = None
             
    def __init__(self, token):
        self.token = token

    def make_query(self, method, payload=None):
        url = 'https://api.telegram.org/bot%s/%s' % (self.token, method)
        r = requests.post(url, payload)
        return r.json()
        
    def get_me(self):
        response = self.make_query('getMe')
        return response

    def get_updates(self, offset, limit=100, timeout=0):
        response = self.make_query('getUpdates', {'offset': offset, 'limit': limit, 'timeout': timeout})
        return response

    def set_webhook(self, url):
        response = self.make_query('setWebhook', {'url': url})
        return response

    def delete_webhook(self):
        response = self.make_query('setWebhook')
        return response
        
    def send_message(self, chat_id, text=None, parse_mode=None):
        response = self.make_query('sendMessage', {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode})
        return response