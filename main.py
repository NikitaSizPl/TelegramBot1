from aiogram.utils import executor
from create_bot import dp


# Все сюда импортируем
async def on_startup(_):
    print("Запустился")

    from data_base import sql
    sql.sql_start()

    from handlers import client
    from keyboards import callback

    client.register_handler_client(dp)
    callback.register_callback(dp)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
