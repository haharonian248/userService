from typing import Optional, List

from api.internal_api.poll_service import user_answer_service_api
from api.internal_api.poll_service.model.user_answer_response import UserAnswerResponse
from model.user_answer_request import UserAnswerRequest
from service import user_service


async def get_user_answers_by_user_id(user_id: int) -> Optional[List[UserAnswerResponse]]:
    user_answer_response_list = await user_answer_service_api.get_user_answer(user_id)
    return user_answer_response_list

async def get_count_answers_by_user_id(user_id: int) -> int:
    user_answered_count = await user_answer_service_api.get_count_answered_by_user(user_id)
    return user_answered_count

async def create_user_answer(user_answer_request: UserAnswerRequest):
    print(">>> ENTERED create_user_answer")
    user_registered = await user_service.is_user_registered(user_answer_request.user_id)
    print(user_registered)
    if user_registered:
        print("User registered:", user_registered)
        user_answer_responses = await get_user_answers_by_user_id(user_answer_request.user_id)
        if user_answer_responses is not None:
            print("User answers:", user_answer_responses)
            if any(user_answer_response.q_id == user_answer_request.q_id for user_answer_response in user_answer_responses):
                await update_user_answer(user_answer_request)
                return {"message": "User answer updated"}
            else:
                await user_answer_service_api.insert_user_answer(user_answer_request)
                return {"message": "User answer created"}
        else:
            await user_answer_service_api.insert_user_answer(user_answer_request)
            return {"message": "User answer created"}
    else:
        return {"message": "User isn't registered"}

async def update_user_answer(user_answer_request: UserAnswerRequest):
    await user_answer_service_api.update_user_answer(user_answer_request)