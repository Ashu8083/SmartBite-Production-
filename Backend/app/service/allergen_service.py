from uuid import UUID

from app.repo.allergen_repo import AllergenRepository
from app.schema.allergen_schema import CreateAllergenSchema
from app.exception.custome_exception import AllergyNotFoundException,AllergyAlreadyExist
from app.model.allergen_model import Allergen


class AllergenService:
    def __init__(self,allergen_repository:AllergenRepository):
        self.allergen_repo:AllergenRepository=allergen_repository

    def create_allergen(self,allergen_schema:CreateAllergenSchema):
        existing_allergen=self.allergen_repo.get_allergen_by_name(allergen_schema.name)
        if existing_allergen:
            raise AllergyAlreadyExist("Allergen existed in this name.")

        allergen=Allergen(
            name=allergen_schema.name,
            description=allergen_schema.description
        )

        return self.allergen_repo.create_allergen(allergen)

    def get_all_allergen(self):
        allergen=self.allergen_repo.get_all_alergen()
        return allergen

    def get_allergen_by_id(self,id:UUID):
        allergen=self.allergen_repo.get_allergen_by_id(id)
        return allergen

    def get_allergen_by_name(self,name:str):
        allergen=self.allergen_repo.get_allergen_by_name(name)
        return allergen

    def update_allergen(self,allergen_id:UUID,allergen_schema:CreateAllergenSchema):
        allergen=self.allergen_repo.get_allergen_by_id(allergen_id)

        if allergen is None:
            raise AllergyNotFoundException("Allergy not found in this id.")

        if allergen_schema.name is not None:
            allergen.name = allergen_schema.name

        if allergen_schema.description is not None:
            allergen.description = allergen_schema.description

        return self.allergen_repo.update_allergen(allergen)
        


    def delete_allergen(self,id:UUID):
        allergen=self.allergen_repo.get_allergen_by_id(id)
        self.allergen_repo.delete_allergen(allergen)
        return {
            "message":"Allergen deleted successfully."
        }