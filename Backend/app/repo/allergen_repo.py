from sqlalchemy.orm import Session
from uuid import UUID
from app.model.allergen_model import Allergen

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

    def get_allergen_by_id(self,id:UUID):
        allergen=self.db.query(Allergen).filter(Allergen.id == id).first()
        return allergen

    def get_allergen_by_name(self,name:str):
        allergen=self.db.query(Allergen).filter(Allergen.name == name).first()
        return allergen

    def update_allergen(self,allergen:Allergen):
        self.db.commit()
        self.db.refresh(allergen)
        return allergen

    def delete_allergen(self,allergen:Allergen):
        self.db.delete(allergen)
        self.db.commit()
        return True



    