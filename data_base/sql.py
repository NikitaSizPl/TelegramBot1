import sqlite3 as sql

from create_bot import bot


# Подключение к базе данных
def sql_connect():
    global cursor, connect
    connect = sql.connect(r'data_base/assortiment.db')
    cursor = connect.cursor()
    if connect:
        print('Подключен к SQL')
    else:
        print('Ошибка подключения SQL')


