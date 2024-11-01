from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.utils import i18n, notify_admin
from app.states.states import Comment
from app.data.config import START_PHOTO_ID as start_photo
from app.keyboards import keyboards

comment_router = Router()

@comment_router.callback_query(F.data == 'comment')
async def comment(callback : CallbackQuery, state : FSMContext):
    curr_user = callback.from_user
    await callback.answer(text='COMMENT')
    await callback.message.delete()

    await state.set_state(Comment.text)
    await callback.message.answer(text=f'{(await i18n.get_comm(curr_user.id))}')

@comment_router.message(Comment.text)
async def get_comm(message : Message, state : FSMContext):
    curr_user = message.from_user
    
    await notify_admin.send_comment(curr_user, message)
    await state.clear()
    await message.answer(text=f'{(await i18n.send_comm(curr_user.id))}')
    await message.answer_photo(photo=start_photo, reply_markup=await keyboards.get_menu(curr_user.id))