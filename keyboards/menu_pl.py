from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data_base import sql


def torty_assort_pl() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_assort_pl')
    for i in sql.get_pl_cakes():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'tort_pl_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort


def bent_assort_pl() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_assort_pl')
    for i in sql.get_pl_bent():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'bent_pl_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort


def mak_assortpl() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_assort_pl')
    for i in sql.get_pl_mak():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'mak_pl_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort
