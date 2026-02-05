from typing import List, Optional

from starlette import status
from fastapi import HTTPException

from model.user_answer_request import UserAnswerRequest
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

@router.post("/createUser", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    try:
        await user_service.create_user(user)
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.delete("/deleteUser/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    try:
        await user_service.delete_user(user_id)
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