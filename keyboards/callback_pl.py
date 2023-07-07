from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from create_bot import bot
from data_base import sql
from keyboards import menu_pl, zakaz


async def pl_assort(call: CallbackQuery) -> None:
    if call.data == 'pl_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu_pl.torty_assort_pl())
    elif call.data == 'pl_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu_pl.bent_assort_pl())
    elif call.data == 'pl_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu_pl.mak_assortpl())
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def tort_pl_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('tort_pl_', '')
    result = sql.callback_cakes_pl(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nCena: {price} zl/kg'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.zakaz_pl(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


async def bento_tort_pl_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('bent_pl_', '')
    result = sql.callback_bento_pl(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nCena: {price} zl'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.bzakaz_pl(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


async def mak_pl_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('mak_pl_', '')
    result = sql.callback_mak_pl(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nCena: {price} zl/szt'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.mzakaz_pl(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(pl_assort,
                                       lambda callback_query: callback_query.data.startswith('pl'))
    dp.register_callback_query_handler(tort_pl_assort,
                                       lambda callback_query: callback_query.data.startswith('tort_pl_'))
    dp.register_callback_query_handler(bento_tort_pl_assort,
                                       lambda callback_query: callback_query.data.startswith('bent_pl_'))
    dp.register_callback_query_handler(mak_pl_assort,
                                       lambda callback_query: callback_query.data.startswith('mak_pl_'))
