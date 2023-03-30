from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import menu


# Декоратор Старт
async def send_welcome(message: types.Message):
    # Id пользователя, который контактирует с ботом
    # user_id = message.from_user.id
    # Имя пользователя, который контактирует с ботом
    user_name = message.from_user.first_name
    await bot.send_message(message.from_user.id, f"Привет, {user_name}!\nПеред тобой Plaisir_Bot.\n\nОт "
                                                 f"https://www.instagram.com/plaisir_lublin/ 👩🏼‍🍳",
                           reply_markup=menu.start_menu())


async def admin():
    pass


# Регистратор декораторов в main.py
def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(admin, commands=['admin'])
