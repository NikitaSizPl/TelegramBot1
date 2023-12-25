import handlers.other
from create_bot import bot
from aiogram.types import CallbackQuery
from aiogram import Dispatcher


async def zakaz_tort(call: CallbackQuery):
    await bot.send_message(call.from_user.id, 'Закать кнопка - ОК')



def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(zakaz_tort,
                                       lambda callback_query: callback_query.data.startswith('new_order'))
