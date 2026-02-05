from pydantic import BaseModel


class UserAnswerRequest(BaseModel):
    user_id: int
    q_id: int
    a_id: int