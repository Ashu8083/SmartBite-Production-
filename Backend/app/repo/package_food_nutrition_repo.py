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
        self.db.commit()
        self.db.refresh(package_food_nutrition)
        return package_food_nutrition
    
    def get_package_food_nutrition_by_id(self,package_food_nutrition_by_id:str):
        packagefood_nutrition = self.db.query(PackageFoodNutrient).filter(PackageFoodNutrient.id==package_food_nutrition_by_id).first()
        return packagefood_nutrition
    
    def get_package_food_nutrition_by_package_id(self,package_id:int):
        packagefood_nutrition = self.db.query(PackageFoodNutrient).filter(PackageFoodNutrient.package_id==package_id).all()
        return packagefood_nutrition
    
    def get_package_food_nutrition_by_nutrient_id(self,nutrient_id:int):
        packagefood_nutrition=self.db.query(PackageFoodNutrient).filter(PackageFoodNutrient.nutrient_id==nutrient_id).all()
        return packagefood_nutrition
    
    def update_package_food_nutrient(self,package_food_nutrient:PackageFoodNutrient,update_food_nutrient:UpdatePackageFoodNutrition):
       for field , value in update_food_nutrient.model_dump(exclude_unset=True).items():
           setattr (package_food_nutrient,field,value)
           self.db.add(package_food_nutrient)
           self.db.commit()
           self.db.refresh(package_food_nutrient)
           return package_food_nutrient
    
    def delete_package_food_nutrient(self,delete_nutrient:PackageFoodNutrient):
        
        self.db.delete(delete_nutrient)
        self.db.commit()
        self.db.refresh(delete_nutrient)
        
        return delete_nutrient