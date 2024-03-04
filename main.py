import requests
import json
import pprint
with open("token.txt") as f:
    token = f.read()


from pathlib import Path, WindowsPath
import random
def getRandomImg(dir: str) -> WindowsPath:
    dirPath = Path.cwd()/dir
    fileinfo = []
    for file in dirPath.rglob('*'):
       fileinfo.append(file.name)
    return dirPath.joinpath(random.choice(fileinfo))




from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Создаем объекты бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher()

key1 = KeyboardButton(text='Да!')
key2 = KeyboardButton(text='Нет')

keybord = ReplyKeyboardMarkup(keyboard=[[key1, key2]])

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!Меня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

def checkMsg(message: Message)->bool:
    res = False
    with open('banWords.txt', encoding='utf-8') as f:
        banWords = f.read().split()
    if message.text:
        userText = message.text.split()
        for word in userText:
            if word in banWords:
                res = True
    return res
def banFilter(userText: str) -> str:
    with open('banWords.txt', encoding='utf-8') as f:
        banWords = f.read().split()
    filteredMes = userText
    for word in userText.split():
        if word in banWords:
            filteredMes = filteredMes.replace(word, "*" * len(word))
    return filteredMes
@dp.message(checkMsg)
async def process_ban(message: Message):
    textReplace = (f'{message.from_user.first_name} просил передать: \n'
                   f'<i>{banFilter(message.text)}</i>')
    await message.delete()
    photo = FSInputFile(getRandomImg('img'))
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await bot.send_message(chat_id=message.from_user.id, text=textReplace, parse_mode='HTML')

def pelmenFilter(message: Message) -> bool:
    return message.text == 'пельмень'

@dp.message(pelmenFilter)
async def send_echo(message: Message):
    await message.answer(text="Хочешь пельмешки?", reply_markup=keybord)

@dp.message(F.text == 'Да!')
async def send_echo(message: Message):
    await message.answer(text="Мммм… Пельмешки... \n Со сметанкой...", reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
#    await message.send_copy()


if __name__ == '__main__':
    dp.run_polling(bot)
