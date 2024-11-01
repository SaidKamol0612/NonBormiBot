from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from app.utils import i18n
from app.states.states import Lang
from app.data.config import START_PHOTO_ID as start_photo
from app.data.config import DISTRICTS_PHOTO_ID as districts_photo
from app.keyboards import keyboards as mkb
from app.services import district_service as ds
from app.services import shop_service as shs
from app.services import user_service as us
from app.utils.clear_messages import add_chat_id, add_msg_id, clear_all

main_router = Router()

langs = {
    'O\'zbek' : 'uz',
    'Русский' : 'ru'
}

@main_router.message(CommandStart())
async def cmd_start(message : Message, state : FSMContext):
    curr_user = message.from_user

    await us.set_user(curr_user.id, curr_user.first_name)
    await add_chat_id(curr_user.id)
    
    welcome_info = f'Assalomu alaykum {curr_user.first_name} !'
    welcome_info += f'\n\n"Non bormi..." telegram bo\'tiga xush kelibsiz !'
    welcome_info += f'\n\nBu botda siz : '
    welcome_info += f'\n    🟢Agar siz iste\'molchi bo\'lsangiz : Qaysi do\'konlarida non bor ekanligi haqida ma\'lumot olishingiz mumkin. '
    welcome_info += f'\n    🟡Agar siz do\'kon xodimi bo\'lsangiz : Sizning do\'koningizda non bor ekanligi haqida ma\'lumot berishingiz mumkin. '
    welcome_info += f'\n        - Agar siz o\'z do\'koningizni bo\'tda ro\'yhatdan otkazmoqchi bo\'lsangiz : Bo\'t muallifi bilan bog\'laning. '
    welcome_info += f'\n\nBo\'t muallifi : @Mirsaidov_SS'

    welcome_info += f'\n====================================================='

    welcome_info += f'\n\n"Добро пожаловать в телеграм бот "Non bormi..." !'
    welcome_info += f'\n\nВ этом боте : '
    welcome_info += f'\n    🟢Если вы покупатель : Можете получить информацию о наличии хлеба в магазинах Ташкента. '
    welcome_info += f'\n    🟡Если вы продавец в магазине : Можете дать информацию о наличии хлеба в вашем магазине. '
    welcome_info += f'\n        - Если ваш магазин пока ещё не зарегистрирован в боте : Свяжитесь с автором бота. '
    welcome_info += f'\n\nАвтор бота : @Mirsaidov_SS'

    await message.answer(text=welcome_info)

    ch_lang = 'Iltimos tilni tanlang : '
    ch_lang += '\nПожалуйста выберите язык : '
    await state.set_state(Lang.lang)
    await message.answer(text=ch_lang, reply_markup=mkb.langs)

@main_router.message(F.text.in_(langs.keys()), Lang.lang)
async def ch_lang(message : Message, state : FSMContext):
    await state.clear()
    curr_user = message.from_user
    await message.answer(text="OK", reply_markup=ReplyKeyboardRemove())
    await i18n.set_lang(curr_user.id, langs.get(message.text))
    await message.answer_photo(photo=start_photo, reply_markup=await mkb.get_menu(curr_user.id))

@main_router.callback_query(F.data == 'start_menu')
async def ch_lang(callback : CallbackQuery):
    curr_user = callback.from_user
    await callback.answer('MENU')
    await callback.message.delete()
    
    await callback.message.answer_photo(photo=start_photo, reply_markup=await mkb.get_menu(curr_user.id))

@main_router.callback_query(F.data == 'districts')
async def search_bread(callback : CallbackQuery):
    curr_user = callback.from_user
    await callback.answer((await i18n.get_districts_str(curr_user.id)))
    await clear_all(curr_user.id)
    await callback.message.delete()

    choose_district = f'{(await i18n.get_d_shops(curr_user.id))} : '
    await callback.message.answer_photo(photo=districts_photo, caption=choose_district, reply_markup=await mkb.get_districts(curr_user.id))

@main_router.callback_query(F.data.startswith('district_'))
async def get_district(callback : CallbackQuery):
    curr_user = callback.from_user
    district = await ds.get_district(callback.data.split('_')[1])
    shops = await shs.get_d_shops(district.id)
    await callback.answer('Do\'konlar')
    await callback.message.delete()

    if len(shops) == 0:
        await callback.message.answer(text=f'{(await i18n.get_no_shops(curr_user.id))}')
        await callback.message.answer_photo(photo=start_photo, reply_markup=await mkb.get_menu(curr_user.id))
        return

    msg = await callback.message.answer(text=f'{(await i18n.get_shops(district.name, curr_user.id))} : ')
    await add_msg_id(curr_user.id, msg.message_id)

    for sh in shops:
        shop_photo = await shs.get_photo(sh.id)
        shop_info = f'{sh.name}'
        shop_info += f'\n{await i18n.get_address(curr_user.id)} : {sh.address}'
        shop_info += f'\n{await i18n.get_phone(curr_user.id)} : {sh.phone_num}'
        shop_info += f'\n{await i18n.get_bread(curr_user.id)} : {(await shs.format_info(sh.bread_info, curr_user.id))}'

        msg = await callback.message.answer_photo(photo=shop_photo, caption=shop_info)
        await add_msg_id(curr_user.id, msg.message_id)
    await callback.message.answer(text=f'{(await i18n.get_other_sh(curr_user.id))} : ', reply_markup=await mkb.get_back(curr_user.id))
