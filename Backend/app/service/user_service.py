from Backend.app.repo.user_repo import UserRepository
from Backend.app.schema.user_schema import UserCreateSchema
from Backend.app.model.user_model import Users
class UserService:
    def __init(self,user_repository:UserRepository):
        self.user_repo:UserRepository=user_repository

    def create_user(self,user_schema:UserCreateSchema):
        user=Users(
            id=user_schema.id,
            username=user_schema.username,
            email=user_schema.email,
            password_hash=user_schema.password_hash,
            is_active=user_schema.is_active,
            is_deleted=user_schema.is_deleted
        )
        return self.user_repo.create_user(user)