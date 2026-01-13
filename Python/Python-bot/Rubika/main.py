import requests
import json

token = 'FFDDB0EIWPPSAXETGFYHZXGPJZDTVZIZOUCVTKUYKJBQAJULXIEOTJLZQYUXIQNQ'

url = f'https://botapi.rubika.ir/v3/{token}/getMe'

req = requests.post(url)

json_translate = json.loads(req.text)
json_format = json.dumps(json_translate, indent=2)


print(json_format)


