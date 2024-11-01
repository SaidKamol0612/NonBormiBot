from app.database.models.models import Shop, Admin
from app.database import requests as rq

async def add_shop(data):
    new_shop = Shop(district_id=data['ch_dist'], photo_id=data['get_photo'], name=data['name'], 
                    address=data['address'], phone_num=data['phone_num'], bread_info='yes')
    
    await rq.add_shop(new_shop)
    
    await rq.add_admin(data['admin_password'], data['phone_num'])


async def remove_shop(shop_id):
    await rq.remove_shop(shop_id)