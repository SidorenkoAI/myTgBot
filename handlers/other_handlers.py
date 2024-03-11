from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from lexicon.lexicon import LEXICON_RU

router = Router()

# Этот хэндлер будет срабатывать на любые не обработанные ранее апдейты"
@router.message()
async def send_echo(message: Message):
    await message.answer(LEXICON_RU['not_cmd'])