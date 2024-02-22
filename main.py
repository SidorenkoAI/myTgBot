import requests
import pprint
with open('token.txt') as f:
    token = f.read()

import requests
import time

TOKEN = token
URL = 'https://api.telegram.org/bot'

while True:
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    url_img = data[0]['url']

    response = requests.get(URL + TOKEN + "/getUpdates"+"?offset=-1")
    updates = response.json()

    if updates['result']:
        message = updates['result'][-1]['message']
        chat_id = message['chat']['id']
        text = message['text']

        requests.get(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={url_img}')

        time.sleep(1)
    else:
        print("Боту сегодня еще никто не писал")




