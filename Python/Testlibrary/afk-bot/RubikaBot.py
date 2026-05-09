import httpx
import json
from url import BASE_URL
from env import TOKEN_RUBIKA

class RubikaBot():

    def __init__(self, token):
        
        self.token = token
        self.base_url = BASE_URL.format(token=token)
        self.client = httpx.Client()

    
    

bot = RubikaBot(TOKEN_RUBIKA)
