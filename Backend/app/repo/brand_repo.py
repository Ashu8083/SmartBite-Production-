from sqlalchemy.orm import Session
from uuid import UUID

from app.model.brand_model import Brand


class BrandRepository:
    def __init__(self,db:Session):
        self.db=db

    def create_brand(self,brand:Brand):
        self.db.add(brand)
        self.db.commit()
        self.db.refresh(brand)
        return brand

    def get_all_brand(self):
        brand=self.db.query(Brand).filter().all()
        return brand

    def get_brand_by_id(self,id:int):
        brand=self.db.query(Brand).filter(Brand.id == id).first()
        return brand

    def get_brand_by_name(self,name:str):
        brand=self.db.query(Brand).filter(Brand.name == name).first()
        return brand

    def delete_brand(self,brand:Brand):
        self.db.delete(brand)
        self.db.commit()
        return True
        
    