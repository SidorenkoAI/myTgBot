from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F

router = Router()
# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!Меня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


def pelmenFilter(message: Message) -> bool:
    return message.text == 'пельмень'

@router.message(pelmenFilter)
async def send_echo(message: Message):
    await message.answer(text="Хочешь пельмешки?")

@router.message(F.text == 'Да!')
async def send_echo(message: Message):
    await message.answer(text="Мммм… Пельмешки... \n Со сметанкой...")

