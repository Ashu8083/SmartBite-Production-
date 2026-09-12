from app.repo.user_repo import UserRepository
from app.schema.user_schema import UserCreateSchema
from app.model.user_model import Users
from uuid import UUID

class UserService:
    def __init__(self,user_repository:UserRepository):
        self.user_repo:UserRepository=user_repository

    def create_user(self,user_schema:UserCreateSchema):
        
        user=Users(
            username=user_schema.username,
            email=user_schema.email,
            password_hash=user_schema.password_hash,
            gender=user_schema.gender,
            user_status=user_schema.user_status,
            is_active=user_schema.is_active,
            is_deleted=user_schema.is_deleted
        )
        return self.user_repo.create_user(user)
    
    def get_all_user(self):
        user=self.user_repo.get_all_user()
        return user
    
    def get_user_by_id(self,user_id:UUID):
        user=self.user_repo.get_user_by_id(user_id)
        return user

    def get_user_by_email(self,email:str):
        user=self.user_repo.get_user_by_email(email)
        return user