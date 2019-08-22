from money_bot.utils import models, strings

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


async def get_user_by_id(user_id: int):
    return await models.User.find_one({"user_id": user_id})


async def is_user_in_db(user_id: int):
    return bool(await get_user_by_id(user_id))


async def set_referrer_id(user_id: int, referrer_id: int):
    user = await get_user_by_id(user_id)
    user.referrer_id = referrer_id
    await user.commit()


async def change_money_amount(user_id: int, value: int):
    user = await get_user_by_id(user_id)
    user.money += value
    await user.commit()


async def get_user_money_amount(user_id: int):
    user = await get_user_by_id(user_id)
    return user.money


async def get_user_referees_amount(user_id: int):
    return await models.db.user.count_documents({"referrer_id": user_id})


async def get_user_verify_status(user_id: int):
    if await get_user_referees_amount(user_id) >= config.REFEREES_TO_ENABLE_WITHDRAWAL:
        return strings.VERIFIED_TRUE_LABEL
    return strings.VERIFIED_FALSE_LABEL


async def get_current_task(user_id: int):
    user = await get_user_by_id(user_id)
    if user is None:
        return None
    tasks = await models.Task.find().to_list(length=None)
    if user.current_task_id >= await models.db.task.count_documents({}):
        return None
    return tasks[user.current_task_id]


async def get_next_task(user_id: int):
    user = await get_user_by_id(user_id)
    if user is None:
        return None
    tasks = await models.Task.find().to_list(length=None)
    if user.current_task_id + 1 >= await models.db.task.count_documents({}):
        return None
    user.current_task_id += 1
    await user.commit()
    return tasks[user.current_task_id]
