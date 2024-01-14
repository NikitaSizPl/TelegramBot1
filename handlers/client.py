from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import menu

start_text = """
Для продолжения выберите язык
Для продовження виберіть мову
Aby kontynuować, wybierz język"""

# Декоратор Старт
async def send_welcome(message: types.Message):
    # Id пользователя, который контактирует с ботом
    # user_id = message.from_user.id
    # Имя пользователя, который контактирует с ботом
    # user_name = message.from_user.first_name
    await bot.send_photo(message.from_user.id, photo=open(f'static/logo_done.jpg', 'rb'), caption=start_text, parse_mode='html', reply_markup=menu.start_lang())

# Регистратор декораторов в main.py
def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
