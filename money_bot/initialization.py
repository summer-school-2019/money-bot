import logging

from aiogram import Bot, Dispatcher
from pymongo import MongoClient
from umongo import Instance

try:
    from money_bot.local_config import BOT_TOKEN, DB_HOST, DB_NAME
except ImportError:
    from money_bot.example_config import BOT_TOKEN, DB_HOST, DB_NAME

logging.basicConfig(level=logging.DEBUG)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
db = MongoClient(DB_HOST)[DB_NAME]
instance = Instance(db)
