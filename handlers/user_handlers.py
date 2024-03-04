from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb

router = Router()
# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU['/start'], reply_markup=yes_no_kb)


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['/help'])


def pelmenFilter(message: Message) -> bool:
    return message.text == 'пельмень'

@router.message(pelmenFilter)
async def send_echo(message: Message):
    await message.answer(text="Хочешь пельмешки?")

@router.message(F.text == 'Да!')
async def send_echo(message: Message):
    await message.answer(text="Мммм… Пельмешки... \n Со сметанкой...")

