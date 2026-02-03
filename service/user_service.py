
from typing import Optional, List

from api.internal_api.poll_service import user_answer_service_api
from api.internal_api.poll_service.model.user_answer_response import UserAnswerResponse
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

async def get_user_answers_by_user_id(user_id: int) -> Optional[List[UserAnswerResponse]]:
    user_answer_response_list = await user_answer_service_api.get_user_answer(user_id)
    return user_answer_response_list

async def get_count_answers_by_user_id(user_id: int) -> int:
    user_answered_count = await user_answer_service_api.get_count_answered_by_user(user_id)
    return user_answered_count