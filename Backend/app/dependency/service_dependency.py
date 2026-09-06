from fastapi import Depends
from Backend.app.repo.user_repo import UserRepository
from Backend.app.service.user_service import UserService 
from Backend.app.core.database import get_db


def get_user_service(db=Depends(get_db)):
    user_repository=UserRepository(db)
    user_service=UserService(user_repository)
    return user_service