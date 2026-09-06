from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    id:int
    username:str
    email:str
    password_hash:str
    is_active:bool
    is_deleted:bool