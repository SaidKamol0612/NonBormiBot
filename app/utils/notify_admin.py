import logging
import time

from aiogram import Bot

from app.data.config import TOKEN, AUTHOR

bot = Bot(TOKEN)

async def send_comment(user, msg):
        info = 'Comment :'
        info += f'\nFrom : {user.first_name}'
        info += f'\n{msg.text}'
        info += f"\n{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"
        try:
            await bot.send_message(chat_id=AUTHOR, text=info)

        except Exception as err:
            logging.exception(err)
    