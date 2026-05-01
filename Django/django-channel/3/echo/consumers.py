import json
from channels.generic.websocket import WebsocketConsumer

class EchoConsumers(WebsocketConsumer):

    def connect(self):
        print("=" * 50)
        print("🟢 CONNECT METHOD CALLED! 🟢")
        print("=" * 50)
        self.accept()

        self.send(text_data=json.dumps(
            {
                'type': 'connect',
                'message': 'connect to echo server'
            }
        ))

    def receive(self, text_data):
        self.send(text_data=text_data)

    def disconnect(self, code):
        print(f'websocket connection closed by code:{code}')