from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from create_bot import bot

storage = MemoryStorage()


# Описываем состояния
class OrderState(StatesGroup):
    INSTA = State()
    DELEVIRI = State()
    INFO = State()
    CONFIRMATION = State()


# Обрабатываем команду /order
async def new_order(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Напиши пожалуйста Ваш Instagram')
    await OrderState.INSTA.set()


async def order_insta(message: types.Message, state: FSMContext):
    # Получаем имя пользователя, сохраняем его и переходим к следующему состоянию
    await state.update_data(insta=message.text)
    await OrderState.DELEVIRI.set()
    await message.reply("Доставка (полный адрес) / самовывоз")


async def order_deleviri(message: types.Message, state: FSMContext):
    # Получаем адрес доставки пользователя, сохраняем его и переходим к следующему состоянию
    await state.update_data(deleviri=message.text)
    await OrderState.INFO.set()
    await message.reply("Напишите пожалуйста дополнительную информацию (дата, вес, декорации)")


async def order_info(message: types.Message, state: FSMContext):
    # Получаем дополнительную информацию от пользователя и переходим к подтверждению заказа
    await state.update_data(info=message.text)
    await OrderState.CONFIRMATION.set()

    # Показываем данные заказа и спрашиваем, подтверждает ли он его
    data = await state.get_data()
    confirmation_message = f"instagram: {data['insta']}\nДоставка: {data['deleviri']}\nДополнительно: \n{data['info']}\n\nПодтверждаете заказ?"
    await message.reply(confirmation_message,
                        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
                            [types.KeyboardButton('Да'), types.KeyboardButton('Нет')]
                        ]))


async def order_finish(message: types.Message, state: FSMContext):
    # Получаем ответ пользователя и обрабатываем его
    if message.text == 'Да':
        data = await state.get_data()
        # Если заказ подтвержден, отправляем сообщение об успешном оформлении заказа
        await message.reply("Ваш заказ успешно оформлен!")
        text = f" Новый заказ:\n\ninstagram: {data['insta']}\n\nДоставка: {data['deleviri']}\n\nДоп. инф: {data['info']}"
        await bot.send_message(6622326689, text)
    else:
        # Если заказ не подтвержден, отправляем сообщение о том, что заказ отменен
        await message.reply("Ваш заказ отменен.")

    # Сбрасываем состояние
    await state.finish()


def register_handler_client(dp: Dispatcher):
    dp.register_callback_query_handler(new_order,
                                       lambda callback_query: callback_query.data.startswith('new_order'))
    dp.register_message_handler(order_insta, state=OrderState.INSTA)
    dp.register_message_handler(order_deleviri, state=OrderState.DELEVIRI)
    dp.register_message_handler(order_info, state=OrderState.INFO)
    dp.register_message_handler(order_finish, state=OrderState.CONFIRMATION)
    dp.storage = storage
