import requests
import pprint
with open('token.txt') as f:
    token = f.read()

endPoint = f'https://api.telegram.org/bot{token}/getMe'
res = requests.get(endPoint).json()
pprint.pprint(res)

