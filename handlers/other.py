from aiogram import Dispatcher, types

from aiogram.dispatcher import FSMContext
from create_bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()


# Создаем состояния FSM
class OrderState(StatesGroup):
    insta = State()
    phone = State()
    deleviri = State()
    adress = State()
    add_order = State()


# Обрабатываем команду /order
async def new_order(message: types.Message):
    # Запрашиваем у пользователя информацию о заказе
    await message.answer("Введите информацию о заказе:")
    await OrderState.insta.set()


# Обрабатываем информацию о заказе
async def order_info(message: types.Message, state: FSMContext):
    order_info = message.text
    await state.update_data(order_info=order_info)
    # Отправляем информацию о заказе на ваш аккаунт
    chat_id_nik = 313483483
    chat_id_nikita = 6622326689
    text = f"Новый заказ:\n\n{order_info}"
    await bot.send_message(chat_id_nikita, text)


    # Очищаем состояние FSM
    await state.finish()

    # Отправляем пользователю подтверждение о успешном оформлении заказа
    await message.answer("Ваш заказ успешно оформлен.")


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(new_order, commands=['order'])
    dp.register_message_handler(order_info, state=OrderState.insta)
    dp.storage = storage
