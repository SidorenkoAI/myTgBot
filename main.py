

import asyncio
from aiogram import Bot, Dispatcher
from handlers import other_handlers, user_handlers
from config_data.config import load_config
from keyboards.keyboards import set_main_menu
async def main() -> None:
    config = load_config()
    # Создаем объекты бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    await set_main_menu(bot)
    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

