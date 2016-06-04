import requests

class Bot():
    """
    Create a bot and manage it
    """
    token = None
             
    def __init__(self, token):
        self.token = token

    def make_query(self, method, payload=None):
        """
        Make query to the Telegram API
        """
        url = 'https://api.telegram.org/bot%s/%s' % (self.token, method)
        r = requests.post(url, payload)
        return r.json()
        
    def get_me(self):
        """
        Get bot information
        """
        response = self.make_query('getMe')
        return response

    def get_updates(self, offset, limit=100, timeout=0):
        """This function does something.

        :param name: The name to use.
        :type name: str.
        :param state: Current state to be in.
        :type state: bool.
        :returns:  int -- the return code.
        :raises: AttributeError, KeyError

        """
        response = self.make_query('getUpdates', {'offset': offset, 'limit': limit, 'timeout': timeout})
        return response

    def set_webhook(self, url):
        response = self.make_query('setWebhook', {'url': url})
        return response

    def delete_webhook(self):
        response = self.make_query('setWebhook')
        return response
        
    def send_message(self, chat_id, text=None, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        response = self.make_query('sendMessage', {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'disable_notification': disable_notification, 'reply_to_message_id': reply_to_message_id, 'reply_markup': reply_markup})
        return response
        
    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=False):
        response = self.make_query('forwardMessage', {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'disable_notification': disable_notification, 'message_id': message_id})
        return response