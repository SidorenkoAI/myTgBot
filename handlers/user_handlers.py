from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb
from services.card_deck import Game
from sqlite3 import Connection


router = Router()
game = Game()
# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message, dbConnect: Connection):
    cursor = dbConnect.cursor()
    cursor.execute('INSERT OR IGNORE INTO Users (tgid, username, allgames, wingames) VALUES (?, ?, ?, ?)',
                   (message.from_user.id, message.from_user.full_name, 0, 0))
    dbConnect.commit()
    await message.answer(LEXICON_RU['/start'], reply_markup=yes_no_kb)


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['/help'])


@router.message(Command(commands=['shuffle']))
async def process_shuffle(message: Message):
    try:
        await game.shuffle()
    except:
        await message.answer(text=LEXICON_RU['card_err'])
    else:
        await message.answer(text=LEXICON_RU['start_game'])


@router.message(Command(commands=['card']))
async def process_card(message: Message,  dbConnect: Connection):
    cursor = dbConnect.cursor()
    cursor.execute(f'SELECT allgames, wingames FROM Users WHERE tgid = {message.from_user.id}')
    userInfo = cursor.fetchall()
    allgames = userInfo[0][0] + 1
    wingames = userInfo[0][1]
    try:
        userUrlPhoto, userValue = await game.getCard()
        botUrlPhoto, botValue = await game.getCard()
    except AttributeError:
        await message.answer(text=LEXICON_RU['no_card'])
    else:
        await message.answer(text=LEXICON_RU['user_card'])
        await message.answer_photo(photo=userUrlPhoto)
        await message.answer(text=LEXICON_RU['bot_card'])
        await message.answer_photo(photo=botUrlPhoto)
        winner = game.whoWin(userValue, botValue)
        if winner == 'user':
            await message.answer(text=LEXICON_RU['win'])
            wingames += 1
        elif winner == 'bot':
            await message.answer(text=LEXICON_RU['lose'])
        elif winner == 'draw':
            await message.answer(text=LEXICON_RU['draw'])
        cursor.execute(
            f'UPDATE Users SET allgames = {allgames}, wingames = {wingames} WHERE tgid = {message.from_user.id}')
        dbConnect.commit()