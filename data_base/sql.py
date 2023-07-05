import sqlite3 as sql

from create_bot import bot


# Подключение к базе данных
#def sql_connect():
    #global connect, cursor
    #connect = sql.connect(r'data_base/assortiment.db')
    #cursor = connect.cursor()
    #if connect:
        #print('Подключен к SQL')
    #else:
        #print('Ошибка подключения SQL')


#async def sql_read_torty(self) -> None:
    #for x in cursor.execute(f"SELECT * FROM torty WHERE id = 1").fetchall():
        #await bot.send_photo(self.from_user.id, x[0], x[1], x[2], x[3], x[4])
    #connect.commit()