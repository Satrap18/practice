import httpx
import json
from url import BASE_URL

class RubikaBot():

    def __init__(self, token):
        
        self.token = token
        self.url = BASE_URL.format(token=token)
        self.client = httpx.Client()


    def _make_request(self, method: str, data: dict = None):

        try:
            response = self.client.post(self.url + method, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f'Erorr {method}: {e}')
            raise e

    def getme(self):

        return self._make_request('getMe')

    def get_chat_id(self):

        data = {"limit": 1}
        result = self._make_request('getUpdates', data)
        return result['data']['updates'][0]['chat_id']

    def get_user_id(self):
        

        data = {"limit": 1}
        result = self._make_request('getUpdates', data)
        return result['data']['updates'][0]['new_message']['sender_id']

bot = RubikaBot()

print(bot.get_user_id())
