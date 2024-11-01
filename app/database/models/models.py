from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from app.data.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class BotUser(Base):
    __tablename__ = 'bot_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()

class District(Base):
    __tablename__ = 'districts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

class Shop(Base):
    __tablename__ = 'shops'

    id: Mapped[int] = mapped_column(primary_key=True)
    district_id: Mapped[int] = mapped_column(ForeignKey(District.id))
    photo_id: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    phone_num: Mapped[str] = mapped_column()
    bread_info: Mapped[str] = mapped_column()

class Admin(Base):
    __tablename__ = 'admins'

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey(Shop.id))
    password: Mapped[str] = mapped_column()

async def async_main():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

