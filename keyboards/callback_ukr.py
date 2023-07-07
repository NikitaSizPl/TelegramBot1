from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from create_bot import bot
from data_base import sql
from keyboards import menu_ukr, zakaz


async def ukr_assort(call: CallbackQuery) -> None:
    if call.data == 'ukr_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu_ukr.torty_assort_ukr())
    elif call.data == 'ukr_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu_ukr.bent_assort_ukr())
    elif call.data == 'ukr_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu_ukr.mak_assort_ukr())
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def torty_ukr_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('tort_ukr_', '')
    result = sql.callback_cakes_ukr(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nЦена: {price} zl/kg'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.zakaz_ukr(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


async def bento_ukr_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('bent_ukr_', '')
    result = sql.callback_bento_ukr(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nЦена: {price} zl'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.bzakaz_ukr(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


async def mak_ukr_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('mak_ukr_', '')
    result = sql.callback_mak_ukr(id)
    if result:
        foto = open(f'{result[5]}{id}.jpg', 'rb')
        name = result[1]
        description = result[3]
        price = result[4]
        text = f'''{name}\n\n{description}\n\nЦена: {price} zl/szt'''
        await bot.send_photo(call.from_user.id, photo=foto, caption=text,
                             reply_markup=zakaz.language_zakaz.mzakaz_ukr(call), parse_mode='HTML')
    else:
        await bot.send_message(call.from_user.id, "Name не найдена")


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(ukr_assort,
                                       lambda callback_query: callback_query.data.startswith('ukr'))
    dp.register_callback_query_handler(torty_ukr_assort,
                                       lambda callback_query: callback_query.data.startswith('tort_ukr_'))
    dp.register_callback_query_handler(bento_ukr_assort,
                                       lambda callback_query: callback_query.data.startswith('bent_ukr_'))
    dp.register_callback_query_handler(mak_ukr_assort,
                                       lambda callback_query: callback_query.data.startswith('mak_ukr_'))
