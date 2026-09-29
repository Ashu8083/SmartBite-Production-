from sqlalchemy.orm import Session
from app.model.package_food_model import PackageFood
from app.schema.packaged_food_schema import PackagedFoodSchema,UpdatePackageFood

class PackagedFoodRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_packaged_food_repo(self,create_packagedFood:PackagedFoodSchema):
        packaged_food=PackageFood(
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
        
        self.db.add(packaged_food)
        self.db.flush()
        return packaged_food
    
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
    
    def updated_package_food(self,package_food :PackageFood,package_food_update:UpdatePackageFood):
        for field , value in package_food_update.model_dump(exclude_unset=True).items():
            setattr(package_food,field,value)
        self.db.add(package_food)
        self.db.flush()
        self.db.flush(package_food)
        return package_food
    
    def delete_package_food(self,package_food_id:int):
        deleted_food=self.db.query(PackageFood).filter(PackageFood.id==package_food_id).first
        if deleted_food is None:
            return None
        
        self.db.delete(deleted_food)
        self.db.flush()
        
        return deleted_food