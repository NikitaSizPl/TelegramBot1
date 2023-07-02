from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from create_bot import bot
from data_base import sql
from keyboards import menu


async def rus_assort(call: CallbackQuery) -> None:
    if call.data == 'rus_ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_torty.torty_assort_rus(call))
    elif call.data == 'rus_ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_bentotorty.bento_torty_rus(call))
    elif call.data == 'rus_ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu.language_assort_makarony.makarony_rus(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def cakes_rus(call: CallbackQuery) -> None:
    if call.data == 'tor_Snick_rus':
        #await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.cakes_sql.sql_read_cakes(call)
        # bot.send_message(message.from_user.id)


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(rus_assort, lambda callback_query: callback_query.data.startswith('rus'))
    dp.register_callback_query_handler(cakes_rus, lambda callback_query: callback_query.data.startswith('tor'))