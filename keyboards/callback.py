from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from create_bot import bot
from data_base import sql
from keyboards import menu



async def call_start_lang(call: CallbackQuery) -> None:
    if call.data == 'lang_btn_rus':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_rus(call))
    elif call.data == 'lang_btn_ukr':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_ukr(call))
    elif call.data == 'lang_btn_pl':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_pl(call))
    elif call.data == 'lang_btn_eng':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_eng(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def cancel_back(call: CallbackQuery) -> None:
    if call.data == 'back_lang_menu':
        await call.message.edit_reply_markup(reply_markup=menu.start_lang())
    elif call.data == 'back_assort_rus':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_rus(call))
    elif call.data == 'back_assort_ukr':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_ukr(call))
    elif call.data == 'back_assort_pl':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_pl(call))
    elif call.data == 'back_assort_eng':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort.pod_menu_eng(call))
    elif call.data == 'back_torty_rus':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_rus(call))
    elif call.data == 'back_torty_ukr':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_ukr(call))
    elif call.data == 'back_torty_pl':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_pl(call))
    elif call.data == 'back_torty_eng':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_eng(call))
    elif call.data == 'back_btorty_rus':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_rus(call))
    elif call.data == 'back_btorty_ukr':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_ukr(call))
    elif call.data == 'back_btorty_pl':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_pl(call))
    elif call.data == 'back_btorty_eng':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_eng(call))
    elif call.data == 'back_mak_rus':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_rus(call))
    elif call.data == 'back_mak_ukr':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_ukr(call))
    elif call.data == 'back_mak_pl':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_pl(call))
    elif call.data == 'back_mak_eng':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_eng(call))

def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(call_start_lang, lambda callback_query: callback_query.data.startswith('lang'))
    dp.register_callback_query_handler(cancel_back, lambda callback_query: callback_query.data.startswith('back'))
