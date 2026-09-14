from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.service.user_service import UserService 
from app.repo.packaged_food_repo import PackagedFoodRepository
from app.service.package_food_service import PackagedFoodService
from app.core.database import get_db


def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service

def get_package_food_service(db=Depends(get_db)):
    package_food_repository=PackagedFoodRepository(db)
    package_food_service=PackagedFoodService(package_food_repository)
    return package_food_service