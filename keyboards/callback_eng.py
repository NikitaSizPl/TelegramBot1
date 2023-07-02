from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from keyboards import menu


async def eng_assort(call: CallbackQuery) -> None:
    if call.data == 'eng_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_eng(call))
    elif call.data == 'eng_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_eng(call))
    elif call.data == 'eng_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_eng(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(eng_assort, lambda callback_query: callback_query.data.startswith('eng'))