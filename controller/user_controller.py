from typing import List, Optional

from starlette import status
from fastapi import APIRouter, HTTPException

from api.internal_api.poll_service import user_answer_service_api
from api.internal_api.poll_service.model.user_answer_response import UserAnswerResponse

from fastapi import APIRouter

from model.user import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/user_id/{user_id}", response_model=User)
async def get_user_by_id(user_id: int) -> Optional[User]:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with user id {user_id} not found")
    return user

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    try:
        await user_service.create_user(user)
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.delete("/user_id/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    try:
        deleted = await user_service.delete_user(user_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail=f"User with user id {user_id} not found")
        ## should include deleting user answers
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.put("/user_id/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id: int, user: User):
    try:
        return await user_service.update_user(user_id, user)
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.put("/user_id/{user_id}/register", status_code=status.HTTP_202_ACCEPTED)
async def register_user(user_id: int):
    try:
        return await user_service.register_user(user_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"User with user id {user_id} not found")

@router.get("/userAnswers/{user_id}", response_model=List[UserAnswerResponse])
async def get_user_answers_by_user_id(user_id: int) -> Optional[List[UserAnswerResponse]]:
    result = await user_service.get_user_answers_by_user_id(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {user_id} not found")

@router.get("/numberOfAnsweredQuestions/{user_id}", response_model=int)
async def get_count_answers_by_user_id(user_id: int) -> int:
    result = await user_service.get_count_answers_by_user_id(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {user_id} not found")

