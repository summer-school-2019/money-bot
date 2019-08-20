from money_bot.utils import models


async def get_current_user(user_id: int):
    return await models.User.find_one({"user_id": user_id})


async def get_current_task(user_id: int):
    user = await get_current_user(user_id)
    if user is None:
        return None
    tasks = await models.Task.find().to_list(length=None)
    if user.current_task_id >= await models.db.task.count_documents({}):
        return None
    return tasks[user.current_task_id]


async def get_next_task(user_id: int):
    user = await get_current_user(user_id)
    if user is None:
        return None
    tasks = await models.Task.find().to_list(length=None)
    if user.current_task_id + 1 >= await models.db.task.count_documents({}):
        return None
    user.current_task_id += 1
    await user.commit()
    return tasks[user.current_task_id]
