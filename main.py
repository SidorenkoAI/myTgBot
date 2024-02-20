import requests
import pprint
with open('token.txt') as f:
    token = f.read()

#получить информацию по всем событиям (апдейтам)
endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(endPoint).json()['result']
pprint.pprint(response)

#сформировать приветствие и узнать chat_id
mes = f'Привет, {response[0]['message']['from']['first_name']}!'
chatID = response[0]['message']['chat']['id']

#отправить сообщение в чат
endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
params = {'chat_id': chatID, 'text': mes}
response = requests.get(endPoint, params=params)
