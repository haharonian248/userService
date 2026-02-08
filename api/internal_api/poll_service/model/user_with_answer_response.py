from typing import List, Optional

from pydantic import BaseModel

from api.internal_api.poll_service.model.user_answer_response import UserAnswerResponse
from model.user_response import UserResponse


class UserWithAnswerResponse(BaseModel):
    message: Optional[str] = None
    user: UserResponse
    answers: Optional[List[UserAnswerResponse]] = None