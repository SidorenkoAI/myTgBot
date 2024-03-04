from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F

router = Router()

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
#    await message.send_copy()