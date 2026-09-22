from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.repo.user_device_repo import UserDeviceRepo
from app.service.user_service import UserService 
from app.service.user_device_service import UserDeviceService
from app.service.user_service import UserService 
from app.repo.packaged_food_repo import PackagedFoodRepository
from app.service.package_food_service import PackagedFoodService
from app.repo.packaged_food_allergen_repo import PackageFoodAllergenRepository
from app.service.package_food_allergen_service import PackageFoodAllergenService
from app.repo.allergen_repo import AllergenRepository
from app.service.allergen_service import AllergenService
from app.core.database import get_db


def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service

def get_user_device_service(db=Depends(get_db)):
    user_device_repository = UserDeviceRepo(db)
    user_service = UserDeviceService(user_device_repository)
    return user_service
    
def get_package_food_service(db=Depends(get_db)):
    package_food_repository=PackagedFoodRepository(db)
    package_food_service=PackagedFoodService(package_food_repository)
    return package_food_service

def get_package_food_allergen_service(db=Depends(get_db)):
    package_food_allergen_repo=PackageFoodAllergenRepository(db)
    package_food_allergen_service=PackageFoodAllergenService(package_food_allergen_repo)
    return package_food_allergen_service

def get_allergen_service(db=Depends(get_db)):
    allergen_repository=AllergenRepository(db)
    allergen_service=AllergenService(allergen_repository)
    return allergen_service


