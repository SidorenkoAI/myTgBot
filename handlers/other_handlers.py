from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F

router = Router()

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    await message.answer('Я не понимать..')