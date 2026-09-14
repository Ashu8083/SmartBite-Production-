from sqlalchemy.orm import Session
from app.model.package_food_model import PackageFood
from app.schema.packaged_food_schema import PackagedFoodSchema,UpdatePackageFood

class PackagedFoodRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_packaged_food_repo(self,create_packagedFood:PackagedFoodSchema):
        packagedfood=PackageFood(
            brand_id=create_packagedFood.brand_id,
            barcode=create_packagedFood.barcode,
            image_url=create_packagedFood.image_url,
            price=create_packagedFood.price,
            category_id=create_packagedFood.category_id,
            allergens_id=create_packagedFood.allergens_id,
            serving_size=create_packagedFood.serving_size,
            serving_unit=create_packagedFood.serving_unit,
            quantity=create_packagedFood.quantity,
            quantity_unit=create_packagedFood.quantity_unit,
            food_claims=create_packagedFood.food_claims
        )
        
        self.db.add(packagedfood)
        self.db.flush()
        return packagedfood
    
    def get_package_food_by_id(self,package_food_id:int):
        package_food=self.db.query(PackageFood).filter(PackageFood.id == package_food_id).first()
        return package_food
    
    def get_package_food_barcode(self,barcode:str):
        package_food=self.db.query(PackageFood).filter(PackageFood.barcode == barcode).first()
        return package_food
    
    def get_package_food_by_brand_id(self,brand_id:str):
        package_food=self.db.query(PackageFood).filter(PackageFood.brand_id == brand_id).all()
        return package_food
    
    def get_package_food_by_category_id(self,category_id:int):
        package_food=self.db.query(PackageFood).filter(PackageFood.category_id == category_id).first()
        return package_food
    
    def updated_package_food(self,package_food_id:int,package_food:UpdatePackageFood):
        existing_food=self.db.query(PackageFood).filter(PackageFood.id==package_food_id).first()
        if existing_food is None:
            return None
        existing_food.brand_id=package_food.brand_id,
        existing_food.barcode=package_food.barcode,
        existing_food.image_url=package_food.image_url,
        existing_food.price=package_food.price,
        existing_food.category_id=package_food.category_id,
        existing_food.allergens_id=package_food.allergens_id,
        existing_food.serving_size=package_food.serving_size,
        existing_food.serving_unit=package_food.serving_unit,
        existing_food.quantity=package_food.quantity,
        existing_food.quantity_unit=package_food.quantity_unit,
        existing_food.food_claims=package_food.food_claims
        
        self.db.flush()
        return existing_food
    
    def delete_package_food(self,package_food_id:int):
        deleted_food=self.db.query(PackageFood).filter(PackageFood.id==package_food_id).first
        if deleted_food is None:
            return None
        
        self.db.delete(deleted_food)
        self.db.flush()
        
        return deleted_food