"""
Create 
Read
Update
Delete 
"""
from user.schemas import createUser # type: ignore

def create_user(user_in: createUser):
    user = user_in.model_dump()
    return{
        "succsess": True,
        "user": user,
    }