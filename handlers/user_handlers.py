from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb
from services.words_game import wordGame
from sqlite3 import Connection
import pprint


router = Router()
game = wordGame()
# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message, dbConnect: Connection):
    # cursor = dbConnect.cursor()
    # cursor.execute('INSERT OR IGNORE INTO Users (tgid, username, allgames, wingames) VALUES (?, ?, ?, ?)',
    #                (message.from_user.id, message.from_user.full_name, 0, 0))
    # dbConnect.commit()
    await message.answer(LEXICON_RU['/start'], reply_markup=yes_no_kb)



# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['/help'])

@router.message(Command(commands=["word"]))
async def process_start_command(message: Message, dbConnect: Connection):
    # cursor = dbConnect.cursor()
    # cursor.execute('INSERT OR IGNORE INTO Users (tgid, username, allgames, wingames) VALUES (?, ?, ?, ?)',
    #                (message.from_user.id, message.from_user.full_name, 0, 0))
    # dbConnect.commit()
    if game.status:
        await message.answer(text='Игра уже запущена! Отгадывайте слово')
        return
    try:
        msg = await game.getWord()
    except:
        msg = 'У меня нет слов (('
    await message.answer(text=msg)

@router.message(lambda message: len(message.text) == 1 and game.status)
async def process_check_symb(message: Message, dbConnect: Connection):
    answer = game.checkSymb(message.text)
    if answer == 'win':
        await message.answer(text=f'Победил {message.from_user.full_name}!')
    elif answer:
        await message.answer(text=answer)
        await message.answer(text=f'Использованные символы: {game.getUsedSymbols()}')
    else:
        await message.answer(text=game.stop())

@router.message(lambda message: message.text == game.word)
async def process_win(message: Message, dbConnect: Connection):
    game.stop()
    await message.answer(text=f'Победил {message.from_user.full_name}!')

#
# @router.message(Command(commands=['stat']))
# async def process_card(message: Message,  dbConnect: Connection):
#     cursor = dbConnect.cursor()
#     cursor.execute(f'SELECT * FROM Users')
#     usersInfo = cursor.fetchall()
#     usersInfoSorted = sorted(usersInfo, key=lambda x: x[4]/x[3] if x[3] != 0 else 0, reverse=True)
#     place = 1
#     for user in usersInfoSorted:
#         if user[1] == message.from_user.id:
#             myPlace = place
#             if user[3]:
#                 myWinPercent = round((user[4] / user[3]) * 100, 2)
#             else:
#                 myWinPercent = 0
#         place += 1
#     await message.answer(text=f'Ваш процент побед {myWinPercent}, вы находитесь на {myPlace} месте')
