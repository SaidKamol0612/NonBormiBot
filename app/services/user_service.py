from app.database import requests as rq

async def set_user(user_id, user_name):
    await rq.set_user(user_id, user_name)