from pydantic import BaseModel

class QuestionAnswerUserCountResponse(BaseModel):
    q_id: int
    q_text: str
    a_id: int
    a_text: str
    user_count: int