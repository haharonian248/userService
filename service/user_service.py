
from typing import Optional

from model.user import User

from repository import user_repository


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_by_id(user_id)

async def create_user(user: User):
    await user_repository.create_user(user)

async def update_user(user_id: int, user: User):
    await user_repository.update_user(user_id,user)

async def register_user(user_id: int):
    await user_repository.register_user(user_id)
    return {"message": "User registered", "user_id": user_id}

async def delete_user(user_id: int):
    deleted_rows = await user_repository.delete_user(user_id)
    return deleted_rows
    ## ADD DELETING ALL ANSWERS FROM THE USER WITH USER_ID