from app.database import requests as rq

async def get_admin(password):
    return await rq.get_admin(password)