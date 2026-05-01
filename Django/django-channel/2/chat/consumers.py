import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connect',
            'message': 'You are connected'  
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('message:', message)
        
        self.send(text_data=json.dumps({
            'type': 'reply',
            'message': f'You said: {message}'
        }))