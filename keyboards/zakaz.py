from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class language_zakaz:
    def __init__(self):
        self.zakaz = None

    def zakaz_rus(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        btn_zakaz = InlineKeyboardButton(text='Заказать', callback_data='new_order')
        btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_torty_rus')
        self.zakaz.add(btn_zakaz, btn_back)
        return self.zakaz

    def bzakaz_rus(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        btn_zakaz = InlineKeyboardButton(text='Заказать', callback_data='new_order')
        btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_btorty_rus')
        self.zakaz.add(btn_zakaz, btn_back)
        return self.zakaz

    def mzakaz_rus(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        btn_zakaz = InlineKeyboardButton(text='Заказать', callback_data='new_order')
        btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_mak_rus')
        self.zakaz.add(btn_zakaz, btn_back)
        return self.zakaz

    def zakaz_ukr(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Замовивши', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_torty_ukr')
        self.zakaz.add(btn_back)
        return self.zakaz

    def bzakaz_ukr(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Замовивши', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_btorty_ukr')
        self.zakaz.add(btn_back)
        return self.zakaz

    def mzakaz_ukr(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Замовивши', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_mak_ukr')
        self.zakaz.add(btn_back)
        return self.zakaz

    def zakaz_pl(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Zamówić', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_torty_pl')
        self.zakaz.add(btn_back)
        return self.zakaz

    def bzakaz_pl(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Zamówić', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_btorty_pl')
        self.zakaz.add(btn_back)
        return self.zakaz

    def mzakaz_pl(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Zamówić', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_mak_pl')
        self.zakaz.add(btn_back)
        return self.zakaz

    def zakaz_eng(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Order', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_torty_eng')
        self.zakaz.add(btn_back)
        return self.zakaz

    def bzakaz_eng(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Order', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_btorty_eng')
        self.zakaz.add(btn_back)
        return self.zakaz

    def mzakaz_eng(self) -> InlineKeyboardMarkup:
        self.zakaz = InlineKeyboardMarkup(row_width=1)
        # btn_zakaz = InlineKeyboardButton(text='Order', callback_data='nn')
        btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_mak_eng')
        self.zakaz.add(btn_back)
        return self.zakaz
