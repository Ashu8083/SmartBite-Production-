from uuid import UUID

from app.repo.brand_repo import BrandRepository
from app.schema.brand_schema import CreateBrandSchema
from app.model.brand_model import Brand
from app.exception.custome_exception import BrandNotFoundException

class BrandService:
    def __init__(self,brand_repository:BrandRepository):
        self.brand_repo:BrandRepository=brand_repository

    def create_brand(self,brand_schema:CreateBrandSchema):
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
            raise BrandNotFoundException("Brand not found in this id.")
        return brand

    def get_brand_by_name(self,name:str):
        brand=self.brand_repo.get_brand_by_name(name)
        if brand is None:
            raise BrandNotFoundException("Brand not found in this name.")
        return brand

    def delete_brand(self,brand_id:int):
        brand=self.brand_repo.get_brand_by_id(brand_id)
        if brand is None:
            raise BrandNotFoundException("This brand_id is invalid. ")
        self.brand_repo.delete_brand(brand)
        return {
            "message":"Brand deleted successfully."
        }
        