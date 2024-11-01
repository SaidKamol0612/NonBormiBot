from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.utils import i18n
from app.services import district_service as ds
from app.services import shop_service as shs

langs = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='O\'zbek'), KeyboardButton(text='Русский')]
], resize_keyboard=True)

dev_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Add shop', callback_data='add_shop'), InlineKeyboardButton(text='Remove shop', callback_data='remove_shop')],
    [InlineKeyboardButton(text='Back', callback_data='start_menu')]
])

async def get_menu(user_id):
    m = (await i18n.get_menu(user_id))
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=m[0], callback_data='districts')],
        [InlineKeyboardButton(text=m[1], callback_data='settings'), InlineKeyboardButton(text=m[2], callback_data='comment')]
    ])

    return menu

async def get_dev_districts(dev_str):
    districts = list(await ds.get_districts())

    d_res = InlineKeyboardBuilder()

    for d in districts:
        d_res.add(InlineKeyboardButton(text=d.name, callback_data=f'dev_district_{dev_str}_{d.id}'))
    d_res.add(InlineKeyboardButton(text='Back', callback_data='start_menu'))

    return d_res.adjust(1).as_markup()

async def dev_shops(d_id):
    shops = list(await shs.get_d_shops(d_id))

    sh_res = InlineKeyboardBuilder()

    for sh in shops:
        sh_res.add(InlineKeyboardButton(text=sh.name, callback_data=f'dev_shop_{sh.id}'))

    return sh_res.adjust(1).as_markup()

async def get_districts(user_id):
    districts = list(await ds.get_districts())

    d_res = InlineKeyboardBuilder()

    for d in districts:
        d_res.add(InlineKeyboardButton(text=d.name, callback_data=f'district_{d.id}'))
    d_res.add(InlineKeyboardButton(text=await i18n.get_back(user_id), callback_data='start_menu'))

    return d_res.adjust(1).as_markup()

async def get_back(user_id):
    back = await i18n.get_back(user_id)
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=back, callback_data='districts')]
    ])

async def admin_menu(user_id, shop_id):
    m = (await i18n.get_admin_menu(user_id))
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=m[0], callback_data=f'yes_{shop_id}'), InlineKeyboardButton(text=m[1], callback_data=f'no_{shop_id}')]
    ])

    return menu

async def settings_menu(user_id):
    m = (await i18n.settings_menu(user_id))
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=m[0], callback_data='change_lang')],
        [InlineKeyboardButton(text=f'{(await i18n.get_back(user_id))}', callback_data='start_menu')]
    ])

    return menu
