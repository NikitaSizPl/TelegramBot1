from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from create_bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

global insta, deleviri, info, chat_id_nikita

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
    insta = message.text
    await state.update_data(insta=insta)
    await OrderState.DELEVIRI.set()
    await message.reply("Доставка (полный адрес) / самовывоз")


async def order_deleviri(message: types.Message, state: FSMContext):
    # Получаем имя пользователя, сохраняем его и переходим к следующему состоянию
    deleviri = message.text
    await state.update_data(deleviri=deleviri)
    await OrderState.INFO.set()
    await message.reply("Напишите пожалуйста дополнительную информацию (дата, вес, декорации)")


async def order_info(message: types.Message, state: FSMContext):
    # Получаем адрес доставки пользователя, сохраняем его и переходим к подтверждению заказа
    info = message.text
    await state.update_data(info=info)
    chat_id_nikita = 6622326689
    await OrderState.CONFIRMATION.set()

    # Получаем все данные заказа
    data = await state.get_data()
    insta = data.get('insta')
    deleviri = data.get('deleviri')
    info = data.get('info')

    # Отправляем пользователю сведения о заказе и спрашиваем, подтверждает ли он его
    confirmation_message = f"instagram: {insta}\nДоставка: {deleviri}\nДополнительно: {info}\n\nПодтверждаете заказ?"
    await message.reply(confirmation_message,
                        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
                            [types.KeyboardButton('Да'), types.KeyboardButton('Нет')]
                        ]))

async def order_finish(message: types.Message, state: FSMContext):
    # Получаем ответ пользователя и обрабатываем его
    if message.text == 'Да':
        # Если заказ подтвержден, отправляем сообщение об успешном оформлении заказа
        await message.reply("Ваш заказ успешно оформлен!")
    else:
        # Если заказ не подтвержден, отправляем сообщение о том, что заказ отменен
        await message.reply("Ваш заказ отменен.")

    # Сбрасываем состояние
    await state.finish()

    text = f" Новый заказ:\n\ninstagram: {insta}\n\nДоставка: {deleviri}\n\nДоп. инф: {info}"
    await bot.send_message(chat_id_nikita, text)

    # Очищаем состояние FSM
    await state.finish()

    # Отправляем пользователю подтверждение о успешном оформлении заказа
    await message.answer("Ваш заказ успешно оформлен.")


def register_handler_client(dp: Dispatcher):
    dp.register_callback_query_handler(new_order,
                                       lambda callback_query: callback_query.data.startswith('new_order'))
    dp.register_message_handler(order_insta, state=OrderState.INSTA)
    dp.register_message_handler(order_deleviri, state=OrderState.DELEVIRI)
    dp.register_message_handler(order_info, state=OrderState.INFO)
    dp.register_message_handler(lambda message: message.text in ['Да', 'Нет'], state=OrderState.CONFIRMATION)
    dp.storage = storage