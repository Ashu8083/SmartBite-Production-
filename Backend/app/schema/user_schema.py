from pydantic import BaseModel,EmailStr
from uuid import UUID
from app.enums.user_enums import UserStatus,Gender
from datetime import datetime

class UserCreateSchema(BaseModel):
    username:str
    email:EmailStr
    password_hash:str
    gender:Gender
    user_status:UserStatus # dont give in frontend
    

class UserResponse(BaseModel):
    username:str
    email:EmailStr
    gender:Gender


class UserUpdate(BaseModel):
    username:str
    email:EmailStr
    gender:Gender
    user_status:UserStatus

    


# response