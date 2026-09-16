from sqlalchemy.orm import Session
from app.model.package_food_allergen_model import PackageFoodAllergen
from app.schema.packaged_food_allergen_schema import PackageFoodAllergenSchema,UpdatePackageFoodAllergen

class PackageFoodAllergenRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_packagefood_allergen(self,create_packgaeFood_allergen:PackageFoodAllergenSchema):
        package_food_allergen=PackageFoodAllergen(
            package_food_id = create_packgaeFood_allergen.package_food_id,
            allergen_id = create_packgaeFood_allergen.allergen_id
        )
        
        self.db.add(package_food_allergen)
        self.db.flush()
        return package_food_allergen
    
    def get_package_food_allergen_by_id(self,package_food_allergen_id:int):
        packagefood_allergen=self.db.query(PackageFoodAllergen).filter(PackageFoodAllergen.id == package_food_allergen_id).first()
        return packagefood_allergen
    
    def get_package_food_allergen_by_package_food_id(self,package_food_id:int):
        packagefood_allergen=self.db.query(PackageFoodAllergen).filter(PackageFoodAllergen.package_food_id==package_food_id).all()
        return packagefood_allergen
    
    def get_package_food_allergen_by_allergen_id(self,allergen_id:int):
        packagefood_allergen=self.db.query(PackageFoodAllergen).filter(PackageFoodAllergen.allergen_id==allergen_id).all()
        return packagefood_allergen
    
    def update_package_food_allergen(self,package_food_allergen_id:int,package_food_allergen:UpdatePackageFoodAllergen):
        exsiting_allergen=self.db.query(PackageFoodAllergen).filter(PackageFoodAllergen.id==package_food_allergen_id).first()
        if exsiting_allergen is None:
            return None
        if package_food_allergen.package_food_id is not None:
            exsiting_allergen.package_food_id=(package_food_allergen.package_food_id)
        if package_food_allergen.allergen_id is None:
            exsiting_allergen.allergen_id=(package_food_allergen.allergen_id)
            
        self.db.flush()
        return exsiting_allergen
    
    def delete_package_food_allergen(self,package_food_allergen_id:int):
        delete_allergen=self.db.query(PackageFoodAllergen).filter(PackageFoodAllergen.id==package_food_allergen_id).first()
        if delete_allergen is None:
            return None
        
        self.db.delete(delete_allergen)
        self.db.flush()
        
        return delete_allergen