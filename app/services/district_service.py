from app.database import requests as rq

async def get_district(d_id):
    return await rq.get_district(d_id)

async def get_districts():
    return await rq.get_districts()