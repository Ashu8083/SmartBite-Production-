from sqlalchemy.orm import Session
from app.model.nutrient_model import Nutrient
from app.schema.nutrient_schema import NutrientSchema,UpdateNutrient

class NutrientRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_nutrient_repo(self,create_nutrient:NutrientSchema):
        nutrient=Nutrient(
            name=create_nutrient.name,
            category=create_nutrient.category,
            unit=create_nutrient.unit
        )
        
        self.db.add(nutrient)
        self.db.flush()
        return nutrient 
    
    def get_nutrient_by_id(self,nutrient_id:int):
        nutrient=self.db.query(Nutrient).filter(Nutrient.id==nutrient_id).first()
        return nutrient
    
    def get_nutrient_by_name(self,name:str):
        nutrient=self.db.query(Nutrient).filter(Nutrient.name==name).first()
        return nutrient
    
    def get_nutrient_by_category(self,category:str):
        nutrient=self.db.query(Nutrient).filter(Nutrient.category==category).all()
        return nutrient
    
    def update_nutrient(self,nutrient_id:int,nutrient:UpdateNutrient):
        existing_nutrient=self.db.query(Nutrient).filter(Nutrient.id==nutrient_id).first()
        if existing_nutrient is None:
            return None
        if existing_nutrient is not None:
            existing_nutrient.name=nutrient.name
        if existing_nutrient is not None:
            existing_nutrient.category=nutrient.category
        if existing_nutrient is not None:
            existing_nutrient.unit=nutrient.unit
        
        return existing_nutrient
    
    def delete_nutrient(self,nutrient_id:int):
        delete_nutrient=self.db.query(Nutrient).filter(Nutrient.id==nutrient_id)
        if delete_nutrient is None:
            return None
        
        self.db.delete(delete_nutrient)
        self.db.flush()
        
        return delete_nutrient