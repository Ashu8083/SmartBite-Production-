from sqlalchemy.orm import Session
from Backend.app.model.package_food_model import PackageFood
from Backend.app.schema.packaged_food_schema import PackagedFoodSchema 

class PackagedFoodRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_packaged_food_repo(self,create_packagedFood:PackagedFoodSchema,id:int):
        packagedfood=PackageFood(
            id=create_packagedFood.id,
            name=create_packagedFood.name,
            description=create_packagedFood.description,
            price=create_packagedFood.price
        )
        
        self.db.add(packagedfood)
        self.db.flush()
        return packagedfood
    
    