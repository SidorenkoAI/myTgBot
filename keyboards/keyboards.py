from aiogram import types
from lexicon.lexicon import LEXICON_RU

yes_key = types.KeyboardButton(text=LEXICON_RU['yes_button'])
no_key = types.KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb = types.ReplyKeyboardMarkup(keyboard=[[yes_key, no_key]])