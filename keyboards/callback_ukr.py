from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from keyboards import menu, zakaz


async def ukr_assort(call: CallbackQuery) -> None:
    if call.data == 'ukr_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_ukr(call))
    elif call.data == 'ukr_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_ukr(call))
    elif call.data == 'ukr_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_ukr(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def tort_rus_assort(call: CallbackQuery) -> None:
    if call.data == 'tukr_Snick':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'tukr_Truskawka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'tukr_Banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def bento_tort_ukr_assort(call: CallbackQuery) -> None:
    if call.data == 'bukr_Wanilia':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'bukr_Czekolada':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'bukr_Karamel':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'bukr_Orzeszki':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'bukr_Biala':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)

async def mak_ukr_assort(call: CallbackQuery) -> None:
    if call.data == 'mukr_Snick':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Ferrero':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Bounty':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Raffaello':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Double_karam':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Capuccino_Baileys':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Raf':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_DorBlue':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Szkolad_wisznia':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Lavanda_pers':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Chiz_golub':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Klubnika_szejk':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Laim_klubnika':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Szokolad_banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Fistaszka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Plombir':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    elif call.data == 'mukr_Limon':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_ukr(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(ukr_assort, lambda callback_query: callback_query.data.startswith('ukr'))
    dp.register_callback_query_handler(tort_rus_assort, lambda callback_query: callback_query.data.startswith('tukr'))
    dp.register_callback_query_handler(bento_tort_ukr_assort, lambda callback_query: callback_query.data.startswith('bukr'))
    dp.register_callback_query_handler(mak_ukr_assort, lambda callback_query: callback_query.data.startswith('mukr'))
