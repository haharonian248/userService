from http.client import HTTPException

import httpx
from typing import List, Optional

from api.internal_api.poll_service.model.question_answer_user_count_response import QuestionAnswerUserCountResponse
from api.internal_api.poll_service.model.user_answer_response import UserAnswerResponse
from model.user_answer_request import UserAnswerRequest
from repository.database import config


async def get_user_answer(user_id: int) -> Optional[List[UserAnswerResponse]]:
    url = f'{config.POLL_SERVICE_BASE_URL}/userAnswers/{user_id}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            data = response.json()

            user_answer_responses = [
                UserAnswerResponse(
                    user_id=user_answer_response.get("user_id"),
                    q_id=user_answer_response.get("q_id"),
                    q_text=user_answer_response.get("q_text"),
                    a_id=user_answer_response.get("a_id"),
                    a_text=user_answer_response.get("a_text")
                )
                for user_answer_response in data
            ]
            return user_answer_responses

        except httpx.HTTPStatusError:
            print(f"No user found with user id: {user_id}")
            return None

async def insert_user_answer(user_answer_request: UserAnswerRequest):
    url = f'{config.POLL_SERVICE_BASE_URL}/insertUserAnswer'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url,json=user_answer_request.dict())
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print("Internal API error:", e.response.text)
            print("Status code:", e.response.status_code)
            raise


async def update_user_answer(user_answer_request: UserAnswerRequest):
    url = f'{config.POLL_SERVICE_BASE_URL}/updateUserAnswer'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url,json=user_answer_request.dict())
            response.raise_for_status()
        except httpx.HTTPStatusError:
            print(f"Unsuccessful in updating user answer")

async def get_count_answered_by_user(user_id: int) -> int:
    url = f'{config.POLL_SERVICE_BASE_URL}/numberOfAnsweredQuestions/{user_id}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            return data
        except httpx.HTTPStatusError:
            print(f"No user found with user id: {user_id}")
            return 0

async def get_total_users_answered_each_option() -> Optional[List[QuestionAnswerUserCountResponse]]:
    url = f'{config.POLL_SERVICE_BASE_URL}/totalCountUsersAnsweredEachOption'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            data = response.json()

            question_answer_user_count_responses = [
                QuestionAnswerUserCountResponse(
                    q_id=question_answer_user_count_response.get("q_id"),
                    q_text=question_answer_user_count_response.get("q_text"),
                    a_id=question_answer_user_count_response.get("a_id"),
                    a_text=question_answer_user_count_response.get("a_text"),
                    user_count=question_answer_user_count_response.get("user_count"),
                )
                for question_answer_user_count_response in data
            ]
            return question_answer_user_count_responses

        except httpx.HTTPStatusError:
            return None

async def delete_user_answers(user_id: int):
    url = f'{config.POLL_SERVICE_BASE_URL}/deleteUserAnswers/{user_id}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url)
            response.raise_for_status()
        except httpx.HTTPStatusError:
            print(f"Unsuccessful in deleting user answers")
