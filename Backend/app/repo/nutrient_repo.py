from typing import Optional

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
        self.db.commit()
        self.db.refresh(nutrient)
        return nutrient 
    
    def get_nutrient_by_id(self,nutrient_id:int):
        nutrient=self.db.query(Nutrient).filter(Nutrient.id==nutrient_id).first()
        return nutrient

    def get_nutrient_by_filter(self,
                               category:  Optional[str] = None,
                               nutrient_name: Optional[str] = None):

        query=self.db.query(Nutrient)
        if nutrient_name is not None:
            query = query.filter(Nutrient.name==nutrient_name)
        if category is not None :
            query = query.filter(Nutrient.category==category)

        return query.all()

    
    def update_nutrient(self,nutrient:Nutrient,nutrient_update:UpdateNutrient):

        for field,value in nutrient_update.model_dump(exclude_unset= True).items():
            setattr(nutrient,field,value)
        self.db.add(nutrient)
        self.db.commit()
        self.db.refresh(nutrient)
        
        return nutrient
    
    def delete_nutrient(self,delete_nutrient:Nutrient):
        self.db.delete(delete_nutrient)
        self.db.commit()
        self.db.refresh(delete_nutrient)
        
        return delete_nutrient