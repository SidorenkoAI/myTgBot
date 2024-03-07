from aiogram import Bot
from aiogram import types
from lexicon.lexicon import LEXICON_RU, LEXICON_CMD

yes_key = types.KeyboardButton(text=LEXICON_RU['yes_button'])
no_key = types.KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb = types.ReplyKeyboardMarkup(keyboard=[[yes_key, no_key]])

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        types.BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_CMD.items()
    ]
    await bot.set_my_commands(main_menu_commands)