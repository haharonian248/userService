
from typing import Optional

from api.internal_api.poll_service import user_answer_service_api
from model.user_request import UserRequest
from model.user_response import UserResponse

from repository import user_repository
from service import user_answer_service


async def get_user_by_id(user_id: int) -> Optional[UserResponse]:
    return await user_repository.get_by_id(user_id)

async def create_user(user: UserRequest):
    await user_repository.create_user(user)
    return {"message": "New user created"}

async def update_user(user_id: int, user: UserRequest):
    await user_repository.update_user(user_id,user)
    return {"message": f"Updated user with user id: {user_id}"}

async def register_user(user_id: int):
    user_exists = await get_user_by_id(user_id)
    if user_exists is None:
        return {"message": "User doesn't exist"}
    else:
        await user_repository.register_user(user_id)
        return {"message": f"User with user id: {user_id} is now registered"}

async def delete_user(user_id: int):
    user_exists = await get_user_by_id(user_id)
    if user_exists:
        user_with_answer_response = await user_answer_service.get_user_answers_by_user_id(user_id)
        if user_with_answer_response is None or user_with_answer_response.answers is None:
            message = "User doesn't have any answered questions"
        else:
            await user_answer_service_api.delete_user_answers(user_id)
            message = "User answers deleted"
        await user_repository.delete_user(user_id)
        return {"message": message + f" and user with user id: {user_id} deleted"}
    else:
        message = "User doesn't exist"
        return {"message": message}

async def is_user_registered(user_id: int) -> bool:
    is_registered = await user_repository.is_user_registered(user_id)
    return is_registered