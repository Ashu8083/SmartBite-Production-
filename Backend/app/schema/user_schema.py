from pydantic import BaseModel,EmailStr

class UserCreateSchema(BaseModel):
    username:str
    email:EmailStr
    is_active:bool
    is_deleted:bool
# response