from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.utils import i18n
from app.keyboards import keyboards
from app.states.states import Lang

settings_router = Router()

@settings_router.callback_query(F.data == 'settings')
async def settings_menu(callback : CallbackQuery):
    curr_user = callback.from_user
    await callback.answer('SETTINGS')
    await callback.message.delete()

    await callback.message.answer(text=f'{(await i18n.get_settings(curr_user.id))} : ', 
                                  reply_markup=await keyboards.settings_menu(curr_user.id))
    
@settings_router.callback_query(F.data == 'change_lang')
async def change_lang(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="LANGUAGE")
    await callback.message.delete()
    ch_lang = 'Iltimos tilni tanlang : '
    ch_lang += '\nПожалуйста выберите язык : '
    await state.set_state(Lang.lang)
    await callback.message.answer(text=ch_lang, reply_markup=keyboards.langs)