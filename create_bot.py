from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import Config

bot = Bot(token=Config.token)
dp = Dispatcher(bot)
