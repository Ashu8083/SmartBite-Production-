from pydantic import BaseModel,EmailStr
from uuid import UUID

class UserCreateSchema(BaseModel):
    username:str
    email:EmailStr
    is_active:bool
    is_deleted:bool
# response