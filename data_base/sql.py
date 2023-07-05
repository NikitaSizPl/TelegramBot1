import sqlite3 as sql


# Подключение к базе данных
def sql_connect():
    global cursor, connect
    connect = sql.connect(r'data_base/assortiment.db')
    cursor = connect.cursor()
    if connect:
        print('Подключен к SQL')
    else:
        print('Ошибка подключения SQL')


def get():
    result = cursor.execute(f'SELECT product_price FROM products WHERE product_id = {id}').fetchone()[0]
    return result

def get_rus_cakes():
    data = cursor.execute('SELECT * FROM cakes').fetchall()
    return data


def get_rus_bent():
    data = cursor.execute('SELECT * FROM bent').fetchall()
    return data


def get_rus_mak():
    data = cursor.execute('SELECT * FROM makaron').fetchall()
    return data


def get_ukr_cakes():
    data = cursor.execute('SELECT * FROM cakes_ukr').fetchall()
    return data


def get_ukr_bent():
    data = cursor.execute('SELECT * FROM bent_ukr').fetchall()
    return data


def get_ukr_mak():
    data = cursor.execute('SELECT * FROM makaron_ukr').fetchall()
    return data
