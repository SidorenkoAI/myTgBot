import requests
import json
import pprint
with open("token.txt") as f:
    token = f.read()







from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

# Создаем объекты бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher()




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

def banFilter(message: Message)->bool:
    res = False
    with open('banWords.txt', encoding='utf-8') as f:
        banWords = f.read().split()
    userText = message.text.split()
    for word in userText:
        if word in banWords:
            res = True
    return res

@dp.message(banFilter)
async def process_ban(message: Message):
    await message.answer(text="Так нельзя!")
    photo = FSInputFile('img/1.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message(lambda message: message.text == 'пельмень')
async def send_echo(message: Message):
    await message.answer(text="Мммм… Пельмешки... \n Со сметанкой...")


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
