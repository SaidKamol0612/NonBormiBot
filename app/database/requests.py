from app.database.models.models import async_session
from app.database.models.models import BotUser, District, Shop, Admin

from sqlalchemy import select, update, delete

async def set_user(user_id, user_name):
    async with async_session() as session:
        user = await session.scalar(select(BotUser).where(BotUser.tg_id == user_id, BotUser.name == user_name))

        if not user:
            session.add(BotUser(tg_id = user_id, name=user_name))
            await session.commit()

async def get_district(d_id):
    async with async_session() as session:
        return await session.scalar(select(District).where(District.id == d_id))

async def get_shops():
    async with async_session() as session:
        return await session.scalars(select(Shop))
    
async def get_shop(shop_id):
    async with async_session() as session:
        return await session.scalar(select(Shop).where(Shop.id == shop_id))

async def get_districts():
    async with async_session() as session:
        return await session.scalars(select(District))
    
async def get_admin(password):
    async with async_session() as session:
        return await session.scalar(select(Admin).where(Admin.password == password))
    
async def set_info_shop(shop_id, info):
    async with async_session() as session:
        stmt = (
            update(Shop)
            .where(Shop.id == shop_id)
            .values(bread_info=info)
            .execution_options(synchronize_session="fetch")
        )
        
        await session.execute(stmt)
        await session.commit()

async def add_shop(shop : Shop):
    async with async_session() as session:
        session.add(shop)
        await session.commit()

async def get_shop_by_num(sh_num):
    async with async_session() as session:
        return await session.scalar(select(Shop).where(Shop.phone_num == sh_num))

async def add_admin(password, sh_num):
    async with async_session() as session:
        shop = await get_shop_by_num(sh_num)
        
        session.add(Admin(shop_id = shop.id, password=password))
        await session.commit()

async def remove_shop(shop_id):
    async with async_session() as session:
        stmt = delete(Shop).where(Shop.id == shop_id)
        await session.execute(stmt)
        await session.commit()