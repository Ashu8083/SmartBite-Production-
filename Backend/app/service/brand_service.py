from uuid import UUID
from fastapi.exceptions import HTTPException
from app.repo.brand_repo import BrandRepository
from app.schema.brand_schema import CreateBrandSchema,BrandUpdate
from app.model.brand_model import Brand
from app.exception.custome_exception import BrandAlreadyExist,BrandNotFoundException

class BrandService:
    def __init__(self,brand_repository:BrandRepository):
        self.brand_repo:BrandRepository=brand_repository

    def create_brand(self,brand_schema:CreateBrandSchema):
        brand_name=self.brand_repo.get_brand_by_name(brand_schema.name)
        if brand_name is None:
            raise BrandAlreadyExist("Brand already exists.")
        brand=Brand(
            name=brand_schema.name,
            logo_url=brand_schema.logo_url,
            website_url=brand_schema.website_url,
            description=brand_schema.description,
            country_name=brand_schema.country_name

        )
        return self.brand_repo.create_brand(brand)

    def get_all_brand(self):
        brand=self.brand_repo.get_all_brand()
        return brand

    def get_brand_by_id(self,id:int):
        brand=self.brand_repo.get_brand_by_id(id)
        if brand is None:
            raise BrandNotFoundException("Brand not found.")
        return brand

    def get_brand_by_name(self,name:str):
        brand=self.brand_repo.get_brand_by_name(name)
        if brand is None:
            raise BrandNotFoundException("Brand not found")
        return brand

    def update_brand(self,brand_id:int,brand_update:BrandUpdate):
        brand=self.brand_repo.get_brand_by_id(brand_id)
        if brand is None:
            raise BrandNotFoundException("Brand not found.")
        brand_object=self.brand_repo.update_brand(brand,brand_update)
        return brand_object

    def delete_brand(self,brand_id:int):
        brand=self.brand_repo.get_brand_by_id(brand_id)
        self.brand_repo.delete_brand(brand)
        return {
            "message":"Brand deleted successfully."
        }
        