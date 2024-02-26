import requests
import pprint
with open('token.txt') as f:
    token = f.read()


def giveAnimation(answer: str) -> str:
    endPoint = f'https://yesno.wtf/api?force={answer}'
    res = requests.get(endPoint).json()
    return res['image']


import time
offset = -2
while True:
    #получить информацию по всем событиям (апдейтам)
    endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
    param = {'offset': offset + 1}
    response = requests.get(endPoint, params=param).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        userText = response['result'][0]['message']['text']
        chatID = response['result'][0]['message']['chat']['id']

        endPoint = f'https://api.telegram.org/bot{token}/sendAnimation'
        params = {'chat_id': chatID, "animation": giveAnimation(userText)}
        res = requests.get(endPoint, params=params)
        pprint.pprint(response['result'])

    time.sleep(1)





