from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class createUser(BaseModel):
    user: Annotated[str, MinLen(3), MaxLen(20)]
    emeil: EmailStr
    
    