from typing import Optional

from model.user import User
from repository.database import database


async def get_by_id(user_id: int) -> Optional[User]:
    query = "SELECT * FROM poll_user WHERE id=:user_id"
    return await database.fetch_one(query, values={"user_id": user_id})

async def create_user(user: User):
    query="""
        INSERT INTO poll_user (first_name, last_name, email, age, address, joining_date, is_registered)
        VALUES (:first_name, :last_name, :email, :age, :address, CURRENT_DATE, FALSE)
    """

    values= {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address
    }
    await database.execute(query, values= values)

async def update_user(user_id: int, user: User):
    query= """
        UPDATE poll_user
        SET first_name=:first_name,
        last_name=:last_name,
        email=:email,
        age=:age,
        address=:address
        WHERE id=:user_id
    """

    values= {
        "user_id": user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address
    }
    await database.execute(query, values=values)

async def delete_user(user_id: int):
    query="DELETE FROM poll_user WHERE id = :user_id"
    return await database.execute(query, values={"user_id": user_id})

async def register_user(user_id: int):
    query="""
        UPDATE poll_user
        SET is_registered=TRUE
        WHERE id=:user_id
    """
    await database.execute(query, values={"user_id": user_id})