from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from keyboards import menu_eng, zakaz


async def eng_assort(call: CallbackQuery) -> None:
    if call.data == 'eng_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu_eng.torty_assort_eng())
    elif call.data == 'eng_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu_eng.bent_assort_eng())
    elif call.data == 'eng_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu_eng.mak_assort_eng())
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def tort_eng_assort(call: CallbackQuery) -> None:
    if call.data == 'teng_Snick':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    elif call.data == 'teng_Truskawka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    elif call.data == 'teng_Banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def bento_tort_eng_assort(call: CallbackQuery) -> None:
    if call.data == 'beng_Wanilia':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    elif call.data == 'beng_Czekolada':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    elif call.data == 'beng_Karamel':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    elif call.data == 'beng_Orzeszki':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    elif call.data == 'beng_Biala':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_eng(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(eng_assort, lambda callback_query: callback_query.data.startswith('eng'))
    dp.register_callback_query_handler(tort_eng_assort, lambda callback_query: callback_query.data.startswith('teng'))
    dp.register_callback_query_handler(bento_tort_eng_assort, lambda callback_query: callback_query.data.startswith('beng'))
