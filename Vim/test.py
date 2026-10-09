import requests

req = requests.get("https://www.lazyvim.org")

print(req.status_code)
