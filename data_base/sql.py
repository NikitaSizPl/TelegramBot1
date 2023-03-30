import sqlite3 as sql

from create_bot import bot


def sql_start():
    global base, cur
    base = sql.connect(r'data_base/assortiment.db')
    cur = base.cursor()
    if base:
        print("Подключен к SQL")
    base.commit()


# Переборка по id - реализовать! if id = 1 -> 1 кнопка, if id = 2 -> 2 кнопка
class torty_bd:
    def __init__(self):
        self.from_user = None

    async def sql_read_torty1(self) -> None:
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 1").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty2(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 2").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty3(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 3").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty4(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 4").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty5(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 5").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty6(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 6").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty7(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 7").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty8(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 8").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty9(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 9").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty10(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 10").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty11(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 11").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty12(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 12").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty13(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 13").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()

    async def sql_read_torty14(self):
        for x in cur.execute(f"SELECT * FROM torty WHERE id = 14").fetchall():
            await bot.send_photo(self.from_user.id, x[0], f'Описание:\n{x[2]}\n\nЦена: {x[3]}zl / 1кг')
        base.commit()


class bentorty_bd:
    def __init__(self):
        self.from_user = None

    async def sql_read_bentorty1(self):
        for x in cur.execute(f"SELECT * FROM bent WHERE id = 1").fetchall():
            await bot.send_message(self.from_user.id, f'Описание:\n{x[1]}\n\nЦена: {x[2]} zl\n')
            base.commit()

    async def sql_read_bentorty2(self):
        string = f"SELECT * FROM bent WHERE id = 2"
        for x in cur.execute(string).fetchall():
            await bot.send_message(self.from_user.id, f'Описание:\n{x[1]}\n\nЦена: {x[2]} zl\n')
            base.commit()

    async def sql_read_bentorty3(self):
        for x in cur.execute(f"SELECT * FROM bent WHERE id = 3").fetchall():
            await bot.send_message(self.from_user.id, f'Описание:\n{x[1]}\n\nЦена: {x[2]} zl\n')
            base.commit()

    async def sql_read_bentorty4(self):
        for x in cur.execute(f"SELECT * FROM bent WHERE id = 4").fetchall():
            await bot.send_message(self.from_user.id, f'Описание:\n{x[1]}\n\nЦена: {x[2]} zl\n')
            base.commit()

    async def sql_read_bentorty5(self):
        for x in cur.execute(f"SELECT * FROM bent WHERE id = 5").fetchall():
            await bot.send_message(self.from_user.id, f'Описание:\n{x[1]}\n\nЦена: {x[2]} zl\n')
            base.commit()


class makaron_bd:
    def __init__(self):
        self.from_user = None

    async def sql_read_makaron1(self):
        for x in cur.execute(f"SELECT * FROM makaron WHERE id = 1").fetchall():
            await bot.send_photo(self.from_user.id, x[4], f'{x[1]}\nЦена: {x[2]}zl / 1шт\n\nМинимальный заказ '
                                                          f'одного вкуса - 10шт\nБоксы с разными вкусами делаются по '
                                                          f'определенным дням.')
            base.commit()

    async def sql_read_makaron2(self):
        for x in cur.execute(f"SELECT * FROM makaron WHERE id = 2").fetchall():
            await bot.send_photo(self.from_user.id, x[4], f'{x[1]}\n\nЦена: {x[2]}zl')
            base.commit()

    # class czizkek_bd:
    # def __init__(self):
    # self.from_user = None

    # async def sql_read_czizkek1(self):
    # for x in cur.execute(f"SELECT * FROM cziz WHERE id = 1").fetchall():
    # await bot.send_photo(self.from_user.id, x[4], f'{x[0]}\n\nОписание:\n{x[1]}\n\nЦена: {x[2]}zl')
    # base.commit()

    # async def sql_read_czizkek2(self):
    # for x in cur.execute(f"SELECT * FROM cziz WHERE id = 1").fetchall():
    # await bot.send_message(self.from_user.id, f'{x[0]}\n\nОписание:\n{x[1]}\n\nЦена: {x[2]}zl')
    # base.commit()

    # async def sql_read_czizkek3(self):
    # for x in cur.execute(f"SELECT * FROM cziz WHERE id = 1").fetchall():
    # await bot.send_message(self.from_user.id, f'{x[0]}\n\nОписание:\n{x[1]}\n\nЦена: {x[2]}zl')
    # base.commit()

    # async def sql_read_czizkek4(self):
    # for x in cur.execute(f"SELECT * FROM cziz WHERE id = 1").fetchall():
    # await bot.send_message(self.from_user.id, f'{x[0]}\n\nОписание:\n{x[1]}\n\nЦена: {x[2]}zl')
    # base.commit()
