from aiogram.types import CallbackQuery
from keyboards import menu
from create_bot import bot
from aiogram import Dispatcher
from data_base import sql



async def pod_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menu.pod_menu())


async def free_data(call: CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await call.message.answer(text="Данный раздел находится в разработке.", reply_markup=menu.free_data())


async def ass_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menu.assort())


async def assort(call: CallbackQuery) -> None:
    if call.data == 'ass_torty':
        await call.message.edit_reply_markup(reply_markup=menu.kb_torty())
    elif call.data == 'ass_bento':
        await call.message.edit_reply_markup(reply_markup=menu.bento_torty())
    elif call.data == 'ass_makaron':
        await call.message.edit_reply_markup(reply_markup=menu.makarony())
    # elif call.data == 'ass_desert':
    # await call.message.edit_reply_markup(reply_markup=menu.deserty())
    elif call.data == 'ass_chiz':
        await call.message.edit_reply_markup(reply_markup=menu.chizkek())
    else:
        await call.message.edit_reply_markup(reply_markup=None)


async def cancel_back(call: CallbackQuery) -> None:
    if call.data == 'back_cancel':
        # await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=None)
    elif call.data == 'back_menu':
        # await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=menu.start_menu())
    elif call.data == 'back_pod_menu':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.answer(text='Меню', reply_markup=menu.pod_menu())
    elif call.data == 'back_assort':
        # await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=menu.assort())
    elif call.data == 'back_kb_torty':
        # await bot.delete_chat_photo(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=menu.kb_torty())
    elif call.data == 'back_kb_bentorty':
        # await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=menu.bento_torty())
    elif call.data == 'back_kb_makaron':
        # await bot.delete_chat_photo(call.message.message_id)
        # await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=menu.makarony())
    elif call.data == 'back_kb_czizkek':
        # await bot.send_photo(call.from_user.id, call.message.message_id)
        # await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.edit_reply_markup(reply_markup=menu.chizkek())


async def assort_torty(call: CallbackQuery) -> None:
    if call.data == 'tor_Snick':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty1(call)
        # bot.send_message(message.from_user.id)
        await bot.send_message(call.from_user.id, text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Truskawka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty2(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Banan':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty3(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Tropikalny':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty4(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Czekol':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty5(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Jogurt':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty6(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_pomarancza':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty7(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_fistaszka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty8(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Oreo':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty9(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_gruszka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty10(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Marchewka':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty11(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Banan-karmel':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty12(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Gruszka-dor':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty13(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))
    elif call.data == 'tor_Miodownik':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.torty_bd.sql_read_torty14(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_torty(call))



async def assort_bentorty(call: CallbackQuery) -> None:
    if call.data == 'ben_Wanilia':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.bentorty_bd.sql_read_bentorty1(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Czekolada':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.bentorty_bd.sql_read_bentorty2(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Karamel':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.bentorty_bd.sql_read_bentorty3(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Orzeszki':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.bentorty_bd.sql_read_bentorty4(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_bentorty(call))
    elif call.data == 'ben_Biala':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.bentorty_bd.sql_read_bentorty5(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_bentorty(call))


async def makarony(call: CallbackQuery) -> None:
    if call.data == 'mak_makaron':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.makaron_bd.sql_read_makaron1(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_makaron(call))
    elif call.data == 'mak_tort':
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await sql.makaron_bd.sql_read_makaron2(call)
        await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_makaron(call))


# async def czizkek(call: CallbackQuery) -> None:
# if call.data == 'Меню':
# await bot.delete_message(call.from_user.id, call.message.message_id)
# await sql.czizkek_bd.sql_read_czizkek1(call)
# await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_czizkek(call))
# elif call.data == 'cziz_Czekoladowy':
# await bot.delete_message(call.from_user.id, call.message.message_id)
# await sql.czizkek_bd.sql_read_czizkek2(call)
# await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_czizkek(call))
# elif call.data == 'cziz_Malina':
# await bot.delete_message(call.from_user.id, call.message.message_id)
# await sql.czizkek_bd.sql_read_czizkek3(call)
# await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_czizkek(call))
# elif call.data == 'cziz_Gruszka':
# await bot.delete_message(call.from_user.id, call.message.message_id)
# await sql.czizkek_bd.sql_read_czizkek4(call)
# await call.message.answer(text='Меню', reply_markup=menu.zakaz.zakaz_czizkek(call))


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(pod_menu, text='pod_menu')
    dp.register_callback_query_handler(ass_menu, text='assort')
    dp.register_callback_query_handler(free_data, text='freedata')
    dp.register_callback_query_handler(assort, lambda callback_query: callback_query.data.startswith('ass'))
    dp.register_callback_query_handler(cancel_back, lambda callback_query: callback_query.data.startswith('back'))
    dp.register_callback_query_handler(assort_torty, lambda callback_query: callback_query.data.startswith('tor'))
    dp.register_callback_query_handler(assort_bentorty, lambda callback_query: callback_query.data.startswith('ben'))
    dp.register_callback_query_handler(makarony, lambda callback_query: callback_query.data.startswith('mak'))
    # dp.register_callback_query_handler(czizkek, lambda callback_query: callback_query.data.startswith('cziz'))
