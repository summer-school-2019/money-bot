from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance, Document, fields
import asyncio

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config

db = AsyncIOMotorClient(config.DB_HOST)[config.DB_NAME]
instance = Instance(db)


@instance.register
class User(Document):

    email = fields.EmailField(required=True, unique=True)
    friends = fields.ListField(fields.ReferenceField("User"))


async def main():
    await User.ensure_indexes()

asyncio.get_event_loop().create_task(main())
