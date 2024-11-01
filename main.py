import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.data.config import TOKEN
from app.database.models.models import async_main
from app.handlers.main_handler import main_router
from app.handlers.admin_handler import admin_router
from app.handlers.settings_menu import settings_router
from app.handlers.comment_menu import comment_router
from app.handlers.developer_menu import developer_router
from app.utils.notify_admin import admin_notify_router

async def main():
    load_dotenv()
    await async_main()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(main_router)
    dp.include_router(admin_router)
    dp.include_router(settings_router)
    dp.include_router(comment_router)
    dp.include_router(developer_router)
    dp.include_router(admin_notify_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stoped.')
        