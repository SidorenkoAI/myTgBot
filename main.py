import requests
import pprint
with open('token.txt') as f:
    token = f.read()


def givePhoto(date: str) -> (str, str):
    endPoint = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY', 'date': date}
    res = requests.get(endPoint, params=params).json()
    explanation = res['explanation']
    urlPhoto = res['url']
    return (urlPhoto, explanation)

def checkDate(date: str) -> bool:
    if len(date) != 10:
        return False
    lst = date.split('-')
    if len(lst) != 3:
        return False
    if not all([len(lst[0]) == 4, len(lst[1]) == 2, len(lst[2]) == 2]):
        return False
    for item in lst:
        if not all(map(lambda x: x.isdigit(), item)):
            return False
    year, month, day = int(lst[0]), int(lst[1]), int(lst[2])
    if not all([2000 <= year <= 2024, 1 <= month <= 12, 1 <= day <= 31]):
        return False
    return True

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
        if checkDate(userText):
            photoURL, photoExp = givePhoto(userText)
            endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
            params = {'chat_id': chatID, 'photo': photoURL}
            res = requests.get(endPoint, params=params)
            endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
            params = {'chat_id': chatID, 'text': photoExp}
            res = requests.get(endPoint, params=params)
        else:
            endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
            params = {'chat_id': chatID, 'text': 'Нужна дата в формате ГГГГ-ММ-ДД'}
            res = requests.get(endPoint, params=params)

    time.sleep(1)





