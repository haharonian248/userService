from pydantic import BaseModel

class UserAnswerResponse(BaseModel):
    user_id: int
    q_id: int
    q_text: str
    a_id: int
    a_text: str