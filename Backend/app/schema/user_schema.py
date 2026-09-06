from pydantic import BaseModel,EmailStr
from uuid import UUID

class UserCreateSchema(BaseModel):
    id:UUID
    username:str
    email:EmailStr
    password_hash:str
    is_active:bool
    is_deleted:bool