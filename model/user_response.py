from datetime import date

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    joining_date: date
    is_registered: bool