from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data.config import AUTHOR_PASSKEY, START_PHOTO_ID as start_photo
from app.keyboards import keyboards
from app.states.states import DEV_MENU

from app.services import district_service as ds
from app.services import developer_service as devs

developer_router = Router()

@developer_router.message(Command('developer'))
async def cmd_developer(message : Message):
    cmd = message.text.split(' ')

    if len(cmd) == 2:
        passkey = cmd[1]
        if passkey == AUTHOR_PASSKEY:
            await message.answer(text='Welcome, Saidkamol !', reply_markup=keyboards.dev_menu)

@developer_router.callback_query(F.data == 'add_shop')
async def add_shop(callback : CallbackQuery, state : FSMContext):
    await callback.answer('DISTRICTS')
    await callback.message.delete()

    await state.set_state(DEV_MENU.add_shop.ch_dist)
    await callback.message.answer(text='Choose district, where you want to add shop : ', reply_markup=await keyboards.get_dev_districts('to_add'))

@developer_router.callback_query(F.data.startswith('dev_district_to_add_'), DEV_MENU.add_shop.ch_dist)
async def add_shop(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="OK")
    d_id = callback.data.split('_')[-1]
    
    await state.update_data(ch_dist=d_id)
    await state.set_state(DEV_MENU.add_shop.get_photo)

    await callback.message.answer(text='Please send photo of shop : ')

@developer_router.message(DEV_MENU.add_shop.get_photo)
async def add_shop(message : Message, state : FSMContext):
    if message.photo[-1] != None:
        await state.update_data(get_photo=message.photo[-1].file_id)
        await state.set_state(DEV_MENU.add_shop.name)

        await message.answer(text='Please send name of new shop : ')

@developer_router.message(DEV_MENU.add_shop.name)
async def add_shop(message : Message, state : FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(DEV_MENU.add_shop.address)

    await message.answer(text='Please send address of new shop : ')

@developer_router.message(DEV_MENU.add_shop.address)
async def add_shop(message : Message, state : FSMContext):
    await state.update_data(address=message.text)
    await state.set_state(DEV_MENU.add_shop.phone_num)

    await message.answer(text='Please send phone number of new shop : ')

@developer_router.message(DEV_MENU.add_shop.phone_num)
async def add_shop(message : Message, state : FSMContext):
    await state.update_data(phone_num=message.text)
    
    await state.set_state(DEV_MENU.add_shop.admin_password)
    await message.answer(text='Please send admin password of new shop : ')

@developer_router.message(DEV_MENU.add_shop.admin_password)
async def add_shop(message : Message, state : FSMContext):
    await state.update_data(admin_password=message.text)
    
    await devs.add_shop(await state.get_data())
    await state.clear()
    await message.answer(text='Success')
    await message.answer_photo(photo=start_photo, reply_markup=await keyboards.get_menu(message.from_user.id))


@developer_router.callback_query(F.data == 'remove_shop')
async def remove_shop(callback : CallbackQuery, state : FSMContext):
    await callback.answer('DISTRICTS')
    await callback.message.delete()

    await state.set_state(DEV_MENU.remove_shop.ch_dist)
    await callback.message.answer(text='Choose district, where you want to remove shop : ', reply_markup=await keyboards.get_dev_districts('to_remove'))

@developer_router.callback_query(F.data.startswith('dev_district_to_remove_'), DEV_MENU.remove_shop.ch_dist)
async def remove_shop(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="OK")
    await callback.message.delete()
    d_id = callback.data.split('_')[-1]

    await state.set_state(DEV_MENU.remove_shop.ch_shop)
    await callback.message.answer(text='Please choose shop : ', reply_markup=await keyboards.dev_shops(d_id))

@developer_router.callback_query(F.data.startswith('dev_shop_'), DEV_MENU.remove_shop.ch_shop)
async def remove_shop(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="OK")
    await callback.message.delete()
    sh_id = callback.data.split('_')[2]
    
    await state.clear()
    await devs.remove_shop(sh_id)
    await callback.message.answer(text='Success')
    await callback.message.answer_photo(photo=start_photo, reply_markup=await keyboards.get_menu(callback.from_user.id))
