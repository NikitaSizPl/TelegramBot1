from aiogram.utils import executor
from create_bot import dp


# Все сюда импортируем
async def on_startup(_):
    print("Запустился")

    from data_base import sql
    #sql.sql_connect()

    from handlers import client
    from keyboards import callback
    from keyboards import callback_rus
    from keyboards import callback_ukr
    from keyboards import callback_pl
    from keyboards import callback_eng

    client.register_handler_client(dp)
    callback.register_callback(dp)
    callback_rus.register_callback(dp)
    callback_ukr.register_callback(dp)
    callback_pl.register_callback(dp)
    callback_eng.register_callback(dp)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
