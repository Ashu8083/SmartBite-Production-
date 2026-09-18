from sqlalchemy.orm import Session
from app.model.package_food_nutrition import PackageFoodNutrient
from app.schema.package_food_nutrition_schema import PackageFoodNutritionSchema,UpdatePackageFoodNutrition

class PackageFoodNutritionRepository:
    
    def __init__(self,db:Session):
        self.db=db
        
    def create_package_food_nutrition(self,create_packagefood_nutrition:PackageFoodNutritionSchema):
        package_food_nutrition=PackageFoodNutrient(
            package_id=create_packagefood_nutrition.package_id,
            nutrient_id=create_packagefood_nutrition.nutrient_id,
            amount=create_packagefood_nutrition.amount
        )
        
        self.db.add(package_food_nutrition)
        self.db.flush()
        return package_food_nutrition
    
    def get_package_food_nutrition_by_id(self,package_food_nutrition_by_id:str):
        packagefood_nutrition = self.db.query(PackageFoodNutrient).filter(PackageFoodNutrient.id==package_food_nutrition_by_id).first()
        return packagefood_nutrition
    
    def get_package_food_nutrition_by_package_id(self,package_id:int):
        packagefood_nutrition = self.db.query(PackageFoodNutrient).filter(PackageFoodNutrient.package_id==package_id).all()
        return packagefood_nutrition
    
    def get_package_food_by_nutrient_id(self,nutrient_id:int):
        packagefood_nutrition=self.db.query(PackageFoodNutrient).filter(PackageFoodNutrient.nutrient_id==nutrient_id).all()
        return packagefood_nutrition
    