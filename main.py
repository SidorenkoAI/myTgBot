from environs import Env
env = Env()
env.read_env()
token = env('BOT_TOKEN')

import asyncio
from aiogram import Bot, Dispatcher
from handlers import other_handlers, user_handlers

async def main() -> None:
    # Создаем объекты бота и диспетчера
    bot = Bot(token=token)
    dp = Dispatcher()
    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())

