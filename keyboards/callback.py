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


async def cakes_rus(call: CallbackQuery) -> None:
    if call.data == 'tor_Snick':
        #await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.cakes_sql.sql_read_cakes(call)
        # bot.send_message(message.from_user.id)
        await call.message.answer(text=f"Ассортимент тортов", reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Truskawka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty2(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Banan':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty3(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Tropikalny':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty4(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Czekol':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty5(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Jogurt':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty6(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_pomarancza':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty7(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_fistaszka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty8(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Oreo':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty9(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_gruszka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty10(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Marchewka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty11(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Banan-karmel':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty12(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Gruszka-dor':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty13(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Miodownik':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty14(call)
        await call.message.answer(text='Ассортимент тортов', reply_markup=menu.zakaz.zakaz_torty(call))


async def assort_bentorty(call: CallbackQuery) -> None:
    if call.data == 'ben_Wanilia':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        with open('data_base/bent/1.jpg', 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
            await sql.bentorty_bd.sql_read_bentorty1(call)
        await call.message.answer(text='Ассортимент бенто тортов', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Czekolada':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        with open('data_base/bent/2.jpg', 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
            await sql.bentorty_bd.sql_read_bentorty1(call)
        await call.message.answer(text='Ассортимент бенто тортов', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Karamel':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        with open('data_base/bent/3.jpg', 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
            await sql.bentorty_bd.sql_read_bentorty1(call)
        await call.message.answer(text='Ассортимент бенто тортов', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Orzeszki':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        with open('data_base/bent/4.jpg', 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
            await sql.bentorty_bd.sql_read_bentorty1(call)
        await call.message.answer(text='Ассортимент бенто тортов', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Biala':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        with open('data_base/bent/5.jpg', 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
            await sql.bentorty_bd.sql_read_bentorty1(call)
        await call.message.answer(text='Ассортимент бенто тортов', reply_markup=menu.zakaz.zakaz_bentorty(call))



def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(call_start_lang, lambda callback_query: callback_query.data.startswith('lang'))
    dp.register_callback_query_handler(cancel_back, lambda callback_query: callback_query.data.startswith('back'))
