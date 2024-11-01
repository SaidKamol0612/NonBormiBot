import logging
import time

from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.data.config import TOKEN, AUTHOR
from app.keyboards import keyboards as kb
from app.utils import i18n

bot = Bot(TOKEN)
admin_notify_router = Router()

async def send_comment(user, msg):
        info = 'Comment :'
        info += f'\nFrom : {user.first_name}'
        info += f'\n{msg.text}'
        info += f"\n{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"
        try:
            await bot.send_message(chat_id=AUTHOR, text=info)

        except Exception as err:
            logging.exception(err)
    