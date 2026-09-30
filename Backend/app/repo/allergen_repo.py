from sqlalchemy.orm import Session
from uuid import UUID
from app.model.allergen_model import Allergen
from app.schema.allergen_schema import AllergenUpdate

class AllergenRepository:
    def __init__(self,db:Session):
        self.db=db

    def create_allergen(self,allergen:Allergen):
        self.db.add(allergen)
        self.db.commit()
        self.db.refresh(allergen)
        return allergen

    def get_all_alergen(self):
        allergen=self.db.query(Allergen).filter().all()
        return allergen

    def get_allergen_by_id(self,id:int):
        allergen=self.db.query(Allergen).filter(Allergen.id == id).first()
        return allergen

    def get_allergen_by_name(self,name:str):
        allergen=self.db.query(Allergen).filter(Allergen.name == name).first()
        return allergen

    def update_allergen(self,allergen:Allergen,allergen_update:AllergenUpdate):
        for field , value in allergen_update.model_dump(exclude_unset=True).items():
            setattr(allergen,field,value)
        self.db.add(allergen)
        self.db.flush()
        self.db.refresh(allergen)
        return allergen

    def delete_allergen(self,allergen:Allergen):
        self.db.delete(allergen)
        self.db.commit()
        return True



    