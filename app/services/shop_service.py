from app.database import requests as rq
from app.utils import i18n

async def get_d_shops(d_id):
    shops = await rq.get_shops()

    res = []
    for sh in shops:
        if sh.district_id == int(d_id):
            res.append(sh)
    return res

async def get_photo(shop_id):
    shop = await rq.get_shop(shop_id)

    return shop.photo_id

async def format_info(info, user_id):
    if info =='yes':
        return await i18n.get_yes(user_id)
    elif info == 'no':
        return await i18n.get_no(user_id)
    
async def set_data(shop_id, info):
    await rq.set_info_shop(shop_id, info)