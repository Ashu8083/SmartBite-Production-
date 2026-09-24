from fastapi import APIRouter,Depends
from app.schema.nutrient_schema import NutrientSchema,UpdateNutrient,NutrientResponse
from app.service.nutrient_service import NutrientService
from app.dependency.service_dependency import get_nutrient_service

nutrient_router=APIRouter(prefix="/nutrient",tags=["nutrient"])
