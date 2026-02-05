
from typing import Optional, List

from api.internal_api.poll_service import user_answer_service_api
from api.internal_api.poll_service.model.user_answer_response import UserAnswerResponse
from model.user import User
from model.user_answer_request import UserAnswerRequest

from repository import user_repository
from service import user_answer_service


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_by_id(user_id)

async def create_user(user: User):
    await user_repository.create_user(user)
    return {"message": "User create"}

async def update_user(user_id: int, user: User):
    await user_repository.update_user(user_id,user)

async def register_user(user_id: int):
    await user_repository.register_user(user_id)
    return {"message": "User registered", "user_id": user_id}

async def delete_user(user_id: int):
    user_exists = get_user_by_id(user_id)
    if user_exists:
        await user_repository.delete_user(user_id)
        user_answer_response_list = await user_answer_service.get_user_answers_by_user_id(user_id)
        if len(user_answer_response_list)==0:
            return {"message": "User doesn't have any answered questions"}
        else:
            await user_answer_service_api.delete_user_answers(user_id)
            return {"message":"User answers deleted"}
    else:
        return {"message": "User doesn't exist"}

async def is_user_registered(user_id: int) -> bool:
    is_registered = await user_repository.is_user_registered(user_id)
    return is_registered