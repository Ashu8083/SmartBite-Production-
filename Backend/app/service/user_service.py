from app.repo.user_repo import UserRepository
from app.schema.user_schema import UserCreateSchema
from app.model.user_model import Users
from uuid import UUID
from fastapi import HTTPException
from datetime import datetime

class UserService:
    def __init__(self,user_repository:UserRepository):
        self.user_repo:UserRepository=user_repository

    def create_user(self,user_schema:UserCreateSchema):
        user_email=self.user_repo.get_user_by_email(user_schema.email)
        if user_email:
            raise HTTPException(
                status_code=409,
                detail="This email is already exist."
            )
        user=Users(
            username=user_schema.username,
            email=user_schema.email,
            password_hash=user_schema.password_hash,
            user_status=user_schema.user_status,
            gender=user_schema.gender
          
            
            


        )
        return self.user_repo.create_user(user)
    
    def get_all_user(self):
        user=self.user_repo.get_all_user()
        return user
    
    def get_user_by_id(self,user_id:UUID):
        user=self.user_repo.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="This user_id is invalid."
            )
        return user

    def get_user_by_email(self,email:str):
        user=self.user_repo.get_user_by_email(email)
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="This email is invalid."
            )
        return user

    def  update_user(self,user_id:UUID,user_schema:UserCreateSchema):
        user=self.user_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User by this id not found"
            )

        return self.user_repo.update_user(user_schema)

    def delete_user(self,user_id:UUID):
        user=self.user_repo.get_user_by_id(user_id)
        self.user_repo.delete_user(user)
        return {
            "message":"user deleted successfully."
        }
