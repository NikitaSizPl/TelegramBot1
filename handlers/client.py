from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import bot
from keyboards import menu
from data_base import sql


# Декоратор Старт
async def send_welcome(message: types.Message):
    # Id пользователя, который контактирует с ботом
    # user_id = message.from_user.id
    # Имя пользователя, который контактирует с ботом
    # user_name = message.from_user.first_name
    await bot.send_message(message.from_user.id, f"Для продолжения выберите язык\n\n"
                                                 f"Для продовження виберіть мову\n\n"
                                                 f"Aby kontynuować, wybierz język\n\n"
                                                 f"To continue, select the language\n\n",

                           reply_markup=menu.start_lang())


# Регистратор декораторов в main.py
def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
