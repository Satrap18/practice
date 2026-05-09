from env import TOKEN_RUBIKA
import httpx
import json
import requests

BASE_URL = f'https://botapi.rubika.ir/v3/{TOKEN_RUBIKA}/'

# data = {
#     "chat_id": "b0FFK3E0QcW03adf07b88c4689a93f5c",
#     "text": "Hello user, this is my text",
# }

# response = httpx.post(BASE_URL, json=data)
# print(response)

# import requests

import requests
import json

url = f"https://botapi.rubika.ir/v3/{BASE_URL}/sendMessage"

data = {
    "chat_id": "u0FFK3E0dd831d37a0fba85f70edb57d",
    "text": "Welcome",
    "inline_keypad": {
        "rows": [
            {
                "buttons": [
                    {
                        "id": "100",
                        "type": "Simple",
                        "button_text": "Add Account"
                    }
                ]
            },
            {
                "buttons": [
                    {
                        "id": "101",
                        "type": "Simple",
                        "button_text": "Edit Account"
                    },
                    {
                        "id": "102",
                        "type": "Simple",
                        "button_text": "Remove Account"
                    }
                ]
            }
        ]
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
