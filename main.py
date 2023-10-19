from aiogram.utils import executor
from create_bot import dp


# Все сюда импортируем
async def on_startup(_):
    print("Запустился")

    from data_base import sql
    sql.sql_connect()
    sql.get_rus_cakes()
    sql.get_rus_bent()
    sql.get_rus_mak()
    sql.get_ukr_mak()
    sql.get_ukr_bent()
    sql.get_ukr_mak()
    sql.get_pl_cakes()
    sql.get_pl_bent()
    sql.get_pl_mak()
    sql.get_eng_mak()
    sql.get_eng_bent()
    sql.get_eng_mak()

    from handlers import client
    from handlers import other
    from handlers import admin
    from keyboards import callback
    from keyboards import callback_rus
    from keyboards import callback_ukr
    from keyboards import callback_pl
    from keyboards import callback_eng

    client.register_handler_client(dp)
    other.register_handler_client(dp)
    admin.register_handler_client(dp)
    callback.register_callback(dp)
    callback_rus.register_callback(dp)
    callback_ukr.register_callback(dp)
    callback_pl.register_callback(dp)
    callback_eng.register_callback(dp)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
