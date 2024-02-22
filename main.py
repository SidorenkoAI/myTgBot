import requests
import pprint
with open('token.txt') as f:
    token = f.read()


# endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
# param = {'offset': -1}
# response = requests.get(endPoint, params=param).json()
# pprint.pprint(response)
# offset работает как срезы в питоне
# a = [1,2,3,4,5,6,7,8]
# print(a[-1:])

def givePhoto(date: str) -> (str, str):
    endPoint = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY', 'date': date}
    res = requests.get(endPoint, params=params).json()
    explanation = res['explanation']
    urlPhoto = res['url']
    return (urlPhoto, explanation)


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
        photoURL, photoExp = givePhoto(userText)
        endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
        params = {'chat_id': chatID, 'photo': photoURL}
        res = requests.get(endPoint, params=params)
        endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chatID, 'text': photoExp}
        res = requests.get(endPoint, params=params)
    time.sleep(1)




# endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
# res = requests.get(endPoint)
# pprint.pprint(res.json())
# endPoint = f'https://api.telegram.org/bot{token}/sendPhoto'
# params = {'chat_id': '598002945', 'photo': urlPhoto}
# res = requests.get(endPoint, params=params)

# #получить информацию по всем событиям (апдейтам)
# endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
# param = {'offset': 29751288}
# response = requests.get(endPoint, params=param).json()
# pprint.pprint(response)

# usersInfo = dict()
# for i in response:
#     chatID = i['message']['chat']['id']
#     userName = i['message']['chat']['first_name']
#     if 'text' in i['message']:
#         userText = i['message']['text']
#     usersInfo[chatID] = [userName, userText]
#
#
# print(usersInfo)
# #отправить сообщение в чат
# endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
# for user in usersInfo:
#     mes = f'Привет, {usersInfo[user][0]}!'
#     params = {'chat_id': user, 'text': mes}
#     res = requests.get(endPoint, params=params)
#
