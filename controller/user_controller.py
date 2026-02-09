from typing import Optional, Any, Coroutine

from starlette import status
from fastapi import HTTPException

from fastapi import APIRouter

from model.user_request import UserRequest
from model.user_response import UserResponse
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/getUserInfo/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int) -> UserResponse:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with user id {user_id} not found")
    return user

@router.post("/createUser", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest):
    try:
        return await user_service.create_user(user)
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.delete("/deleteUser/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_user(user_id: int):
    try:
        result = await user_service.delete_user(user_id)
        return result
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.put("/updateUser/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id: int, user: UserRequest):
    try:
        return await user_service.update_user(user_id, user)
    except Exception:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.put("/registerUser/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def register_user(user_id: int):
    try:
        return await user_service.register_user(user_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"User with user id {user_id} not found")