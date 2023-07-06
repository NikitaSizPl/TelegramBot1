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


def callback_cakes_rus(id):
    query = "SELECT * FROM cakes WHERE callback = :id"
    result = cursor.execute(query, {"id": id}).fetchone()
    return result


def callback_bento_rus(id):
    query = "SELECT * FROM bent WHERE callback = :id"
    result = cursor.execute(query, {"id": id}).fetchone()
    return result


def callback_mak_rus(id):
    query = "SELECT * FROM makaron WHERE callback = :id"
    result = cursor.execute(query, {"id": id}).fetchone()
    return result


def callback_cakes_ukr(id):
    query = "SELECT * FROM cakes_ukr WHERE callback = :id"
    result = cursor.execute(query, {"id": id}).fetchone()
    return result


def callback_bento_ukr(id):
    query = "SELECT * FROM bent_ukr WHERE callback = :id"
    result = cursor.execute(query, {"id": id}).fetchone()
    return result


def callback_mak_ukr(id):
    query = "SELECT * FROM makaron_ukr WHERE callback = :id"
    result = cursor.execute(query, {"id": id}).fetchone()
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


def get_pl_cakes():
    data = cursor.execute('SELECT * FROM cakes_pl').fetchall()
    return data


def get_pl_bent():
    data = cursor.execute('SELECT * FROM bent_pl').fetchall()
    return data


def get_pl_mak():
    data = cursor.execute('SELECT * FROM makaron_pl').fetchall()
    return data


def get_eng_cakes():
    data = cursor.execute('SELECT * FROM cakes_eng').fetchall()
    return data


def get_eng_bent():
    data = cursor.execute('SELECT * FROM bent_eng').fetchall()
    return data


def get_eng_mak():
    data = cursor.execute('SELECT * FROM makaron_eng').fetchall()
    return data
