import requests
import pprint
with open('token.txt') as f:
    token = f.read()

#получить информацию по всем событиям (апдейтам)
endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(endPoint).json()['result']
pprint.pprint(response)

usersInfo = dict()
for i in response:
    chatID = i['message']['chat']['id']
    userName = i['message']['chat']['first_name']
    if 'text' in i['message']:
        userText = i['message']['text']
    usersInfo[chatID] = [userName, userText]


print(usersInfo)
#отправить сообщение в чат
endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
for user in usersInfo:
    mes = f'Привет, {usersInfo[user][0]}!'
    params = {'chat_id': user, 'text': mes}
    res = requests.get(endPoint, params=params)

