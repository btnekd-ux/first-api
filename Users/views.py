from fastapi import APIRouter



from Users.schemas import createUser
from Users import CRUD

router = APIRouter(prefix="/user", tags=["Users"])
@router.post("/")
def create_user(user: createUser):
    return CRUD.create_user(user_in = user)
    