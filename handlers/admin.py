from aiogram import types, Dispatcher

from create_bot import bot


def admin(message: types.Message):
    pass


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(admin, commands=['admin'])
