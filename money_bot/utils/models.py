# pylint: skip-file

import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Document, Instance, fields

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config

db = AsyncIOMotorClient(config.DB_HOST)[config.DB_NAME]
instance = Instance(db)


@instance.register
class User(Document):

    user_id = fields.IntegerField(required=True, unique=True)
    money = fields.IntegerField(default=0)
    first_name = fields.StringField()
    last_name = fields.StringField(allow_none=True)
    username = fields.StringField()
    current_task_id = fields.IntegerField(default=-1)


@instance.register
class Task(Document):

    chat_id = fields.IntegerField(required=True)
    channel_name = fields.StringField()
    url = fields.URLField()


async def main():
    await User.ensure_indexes()
    await Task.ensure_indexes()


asyncio.get_event_loop().create_task(main())
