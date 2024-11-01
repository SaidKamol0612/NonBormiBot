from aiogram.fsm.state import StatesGroup, State

class Lang(StatesGroup):
    lang = State()

class Admin(StatesGroup):
    ent_info = State()

class Comment(StatesGroup):
    text = State()

class AddShop(StatesGroup):
    ch_dist = State()
    get_photo = State()
    name = State()
    address = State()
    phone_num = State()
    admin_password = State()

class RemoveShop(StatesGroup):
    ch_dist = State()
    ch_shop = State()

class DEV_MENU(StatesGroup):
    add_shop = AddShop()
    remove_shop = RemoveShop()