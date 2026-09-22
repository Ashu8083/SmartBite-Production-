from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.service.user_service import UserService 
from app.repo.packaged_food_repo import PackagedFoodRepository
from app.service.package_food_service import PackagedFoodService
from app.repo.packaged_food_allergen_repo import PackageFoodAllergenRepository
from app.service.package_food_allergen_service import PackageFoodAllergenService
from app.repo.package_food_nutrition_repo import PackageFoodNutritionRepository
from app.service.package_food_nutrition_service import PackageFoodNutritionService
from app.core.database import get_db


def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service

def get_package_food_service(db=Depends(get_db)):
    package_food_repository=PackagedFoodRepository(db)
    package_food_service=PackagedFoodService(package_food_repository)
    return package_food_service

def get_package_food_allergen_service(db=Depends(get_db)):
    package_food_allergen_repo=PackageFoodAllergenRepository(db)
    package_food_allergen_service=PackageFoodAllergenService(package_food_allergen_repo)
    return package_food_allergen_service

def get_package_food_nutrition_service(db=Depends(get_db)):
    package_food_nutrition_repo=PackageFoodNutritionRepository(db)
    package_food_nutrition_service=PackageFoodNutritionService(package_food_nutrition_repo)
    return package_food_nutrition_service