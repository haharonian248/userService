from typing import Optional, Any, Coroutine

from api.internal_api.poll_service import user_answer_service_api
from api.internal_api.poll_service.model.user_with_answer_response import UserWithAnswerResponse
from model.user_answer_request import UserAnswerRequest
from service import user_service


async def get_user_answers_by_user_id(user_id: int) -> Optional[UserWithAnswerResponse]:
    user_with_answer_responses = await user_answer_service_api.get_user_answer(user_id)
    return user_with_answer_responses

async def get_count_answers_by_user_id(user_id: int) -> int:
    user_answered_count = await user_answer_service_api.get_count_answered_by_user(user_id)
    return user_answered_count

async def create_user_answer(user_answer_request: UserAnswerRequest)-> Optional[UserWithAnswerResponse] | dict[str, str]:
    user_exist = await user_service.get_user_by_id(user_answer_request.user_id)
    if user_exist:
        user_registered = await user_service.is_user_registered(user_answer_request.user_id)
        if user_registered:
            user_answer_responses = await get_user_answers_by_user_id(user_answer_request.user_id)
            if not user_answer_responses or not user_answer_responses.answers:
                return await user_answer_service_api.insert_user_answer(user_answer_request)
            answers = user_answer_responses.answers
            if any(answer.q_id == user_answer_request.q_id for answer in answers):
                return await update_user_answer(user_answer_request)
            else:
                return await user_answer_service_api.insert_user_answer(user_answer_request)
        else:
            return {"message": "User isn't registered"}
    else:
        return {"message": "User doesn't exist"}


async def update_user_answer(user_answer_request: UserAnswerRequest) -> Optional[UserWithAnswerResponse]:
    print("Updating user answer")
    user_with_answer_response = await user_answer_service_api.update_user_answer(user_answer_request)
    print(user_with_answer_response.answers)
    return user_with_answer_response