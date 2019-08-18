import logging

from aiogram import Bot, Dispatcher
from pymongo import MongoClient
from umongo import Instance

from money_bot.local_config import *

logging.basicConfig(level=logging.DEBUG)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
db = MongoClient(DB_HOST)[DB_NAME]
instance = Instance(db)
