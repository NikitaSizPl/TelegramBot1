from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from create_bot import bot
from data_base import sql
from keyboards import menu_rus, zakaz


async def rus_assort(call: CallbackQuery) -> None:
    if call.data == 'rus_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu_rus.torty_assort_rus())
    elif call.data == 'rus_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu_rus.bent_assort_rus())
    elif call.data == 'rus_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu_rus.mak_assort_rus())
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def torty_rus_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('tort_rus_', '')
    result = sql.callback_cakes_rus(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nЦена: {price} zl/kg'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.zakaz_rus(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


async def bento_rus_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('bent_rus_', '')
    result = sql.callback_bento_rus(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nЦена: {price} zl'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.bzakaz_rus(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


async def mak_rus_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('mak_rus_', '')
    result = sql.callback_mak_rus(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nЦена: {price} zl/szt'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.mzakaz_rus(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(rus_assort,
                                       lambda callback_query: callback_query.data.startswith('rus'))
    dp.register_callback_query_handler(torty_rus_assort,
                                       lambda callback_query: callback_query.data.startswith('tort_rus_'))
    dp.register_callback_query_handler(bento_rus_assort,
                                       lambda callback_query: callback_query.data.startswith('bent_rus_'))
    dp.register_callback_query_handler(mak_rus_assort,
                                       lambda callback_query: callback_query.data.startswith('mak_rus_'))
