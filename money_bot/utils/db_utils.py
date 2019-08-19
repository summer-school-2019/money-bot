from money_bot.utils import models


async def get_current_user(user_id: int):
    return await models.User.find_one({"user_id": user_id})


async def get_current_task(user_id: int):
    user = await get_current_user(user_id)
    if user is None:
        return None
    tasks = models.Task.find()
    if user.current_task_id >= len(tasks):
        return None
    return tasks[user.current_task_id]


async def get_next_task(user_id: int):
    user = await get_current_user(user_id)
    if user is None:
        return None
    tasks = models.Task.find()
    if user.current_task_id + 1 >= len(tasks):
        return None
    user.current_task_id += 1
    await user.commit()
    return tasks[user.current_task_id]
