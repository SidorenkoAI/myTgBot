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


@router.message(F.text == LEXICON_RU['yes_button'])
async def send_echo(message: Message):
    await game.shuffle()


@router.message(F.text == LEXICON_RU['no_button'])
async def send_echo(message: Message):
    urlPhoto, value = await game.getCard()
    await message.answer_photo(photo=urlPhoto)

