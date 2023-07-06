from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data_base import sql


def torty_assort_rus() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_rus')
    for i in sql.get_rus_cakes():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'tort_rus_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort


def bent_assort_rus() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_rus')
    for i in sql.get_rus_bent():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'bent_rus_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort


def mak_assort_rus() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_rus')
    for i in sql.get_rus_mak():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'mak_rus_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort
