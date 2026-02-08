from typing import Optional

from fastapi import APIRouter, HTTPException
from starlette import status

from api.internal_api.poll_service.model.user_with_answer_response import UserWithAnswerResponse
from model.user_answer_request import UserAnswerRequest
from service import user_answer_service

router = APIRouter(
    prefix="/userAnswer",
    tags=["userAnswer"]
)

@router.get("/getUserAnswers/{user_id}", response_model=UserWithAnswerResponse)
async def get_user_answers_by_user_id(user_id: int) -> Optional[UserWithAnswerResponse]:
    result = await user_answer_service.get_user_answers_by_user_id(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {user_id} not found")

@router.get("/numberOfAnsweredQuestions/{user_id}", response_model=int)
async def get_count_answers_by_user_id(user_id: int) -> int:
    result = await user_answer_service.get_count_answers_by_user_id(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {user_id} not found")

@router.post("/insertUserAnswer")
async def create_user_answer(user_answer_request: UserAnswerRequest):
    try:
        result = await user_answer_service.create_user_answer(user_answer_request)
        return result
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/updateUserAnswer", response_model=UserWithAnswerResponse)
async def update_user_answer(user_answer_request: UserAnswerRequest):
    try:
        result = await user_answer_service.update_user_answer(user_answer_request)
        return result
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=400, detail=str(e))
