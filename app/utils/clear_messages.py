from aiogram import Bot
from app.data.config import TOKEN

bot = Bot(token=TOKEN)

chat_messages_id = {}

async def add_chat_id(user_id):
    if user_id not in chat_messages_id:
        chat_messages_id[user_id] = []

async def add_msg_id(user_id, message_id):
    if user_id in chat_messages_id:
        chat_messages_id[user_id].append(message_id)

async def clear_all(user_id):
    if user_id in chat_messages_id:
        for msg_id in chat_messages_id[user_id]:
            try:
                await bot.delete_message(user_id, msg_id)
            except Exception:
                print("Can't delete message!")
        chat_messages_id[user_id].clear()
    else:
        print("User ID not found in chat_messages_id!")
    await bot.session.close()