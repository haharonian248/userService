
from typing import Optional

from model.user import User

from repository import user_repository


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_by_id(user_id)

async def create_user(user: User):
    await user_repository.create_user(user)

# async def update_user(self, user_id: int, userUpdate: UserUpdate):
#     existing_user = await self.user_repository.get_user_by_id(user_id)
#     if not existing_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     update_data = userUpdate.dict(exclude_unset=True)
#
#     for key, value in update_data.items():
#         setattr(existing_user, key, value)
#
#     await self.user_repository.update_user(user_id, existing_user)
#     return existing_user


async def delete_user(user_id: int):
    await user_repository.delete_user(user_id)
    ## ADD DELETING ALL ANSWERS FROM THE USER WITH USER_ID