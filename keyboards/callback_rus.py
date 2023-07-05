from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from create_bot import bot
from keyboards import menu_rus, zakaz
from data_base import sql


async def rus_assort(call: CallbackQuery) -> None:
    if call.data == 'rus_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu_rus.torty_assort_rus())
    elif call.data == 'rus_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu_rus.bent_assort_rus())
    elif call.data == 'rus_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu_rus.mak_assort_rus())
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def cake_rus_assort(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    id = call.data.replace('tort_rus_', '')
    cake = sql.get(id)
    await bot.send_message(call.from_user.id, cake, reply_markup=zakaz.language_zakaz.zakaz_rus(call))


async def bento_tort_rus_assort(call: CallbackQuery) -> None:
    if call.data == 'brus_Wanilia':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.bzakaz_rus(call))
    elif call.data == 'brus_Czekolada':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.bzakaz_rus(call))
    elif call.data == 'brus_Karamel':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.bzakaz_rus(call))
    elif call.data == 'brus_Orzeszki':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.bzakaz_rus(call))
    elif call.data == 'brus_Biala':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.bzakaz_rus(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def mak_rus_assort(call: CallbackQuery) -> None:
    if call.data == 'mrus_Snick':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Ferrero':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Bounty':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Raffaello':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Double_karam':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Capuccino_Baileys':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Raf':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_DorBlue':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Szkolad_wisznia':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Lavanda_pers':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Chiz_golub':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Klubnika_szejk':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Laim_klubnika':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Szokolad_banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Fistaszka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Plombir':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    elif call.data == 'mrus_Limon':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.mzakaz_rus(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(cake_rus_assort,
                                       lambda callback_query: callback_query.data.startswith('tort_rus_'))
    dp.register_callback_query_handler(rus_assort,
                                       lambda callback_query: callback_query.data.startswith('rus'))

    dp.register_callback_query_handler(bento_tort_rus_assort,
                                       lambda callback_query: callback_query.data.startswith('brus'))
    dp.register_callback_query_handler(mak_rus_assort,
                                       lambda callback_query: callback_query.data.startswith('mrus'))
