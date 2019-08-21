from money_bot.utils import models


async def is_user_in_db(user_id: int):
    return await get_user_by_id(user_id) is None


async def set_referrer_id(user_id: int, referrer_id: int):
    user = await get_user_by_id(user_id)
    user.referrer_id = referrer_id
    await user.commit()


async def increase_money_amount(user_id: int, increase_value_amount: int):
    user = await get_user_by_id(user_id)
    user.money += increase_value_amount
    await user.commit()


async def get_user_money_amount(user_id: int):
    user = await get_user_by_id(user_id)
    return user.money


async def get_user_by_id(user_id: int):
    return await models.User.find_one({"user_id": user_id})


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


async def get_user_referees_amount(user_id: int):
    users = await models.User.find_one({"referrer_id": user_id})
    return len(users) if users else 0
