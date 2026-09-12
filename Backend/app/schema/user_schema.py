from pydantic import BaseModel,EmailStr
from uuid import UUID
from app.enums.user_enums import UserStatus,Gender
class UserCreateSchema(BaseModel):
    username:str
    email:EmailStr
    password_hash:str
    gender:Gender
    user_status:UserStatus
    is_active:bool
    is_deleted:bool
    


# response