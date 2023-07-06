from aiogram import Dispatcher
from aiogram.types import CallbackQuery

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


async def tort_pl_assort(call: CallbackQuery) -> None:
    if call.data == 'tpl_Snick':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    elif call.data == 'tpl_Truskawka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    elif call.data == 'tpl_Banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def bento_tort_pl_assort(call: CallbackQuery) -> None:
    if call.data == 'bpl_Wanilia':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    elif call.data == 'bpl_Czekolada':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    elif call.data == 'bpl_Karamel':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    elif call.data == 'bpl_Orzeszki':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    elif call.data == 'bpl_Biala':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_pl(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(pl_assort, lambda callback_query: callback_query.data.startswith('pl'))
    dp.register_callback_query_handler(tort_pl_assort, lambda callback_query: callback_query.data.startswith('tpl'))
    dp.register_callback_query_handler(bento_tort_pl_assort, lambda callback_query: callback_query.data.startswith('bpl'))
