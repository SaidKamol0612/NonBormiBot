from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.services import admin_service as ads
from app.services import shop_service as shs
from app.utils import i18n
from app.keyboards import keyboards
from app.states.states import Admin

admin_router = Router()

@admin_router.message(Command('admin'))
async def cmd_admin(message : Message, state : FSMContext):
    curr_user = message.from_user
    cmd = message.text.split(' ')

    if len(cmd) == 2:
        password = cmd[1]
        admin = await ads.get_admin(password)
        await state.set_state(Admin.ent_info)
        if admin:
            await message.answer(text=f'{(await i18n.get_set_info(curr_user.id))} ?', 
                                 reply_markup=await keyboards.admin_menu(curr_user.id, admin.shop_id))
            
@admin_router.callback_query(Admin.ent_info)
async def set_info(callback : CallbackQuery, state : FSMContext):
    curr_user = callback.from_user
    info = callback.data.split('_')[0]
    shop_id = callback.data.split('_')[1]
    
    await callback.answer(text='OK')
    await callback.message.delete()

    await shs.set_data(shop_id, info)
    await state.clear()
    await callback.message.answer(text=f'{(await i18n.get_success(curr_user.id))}')



