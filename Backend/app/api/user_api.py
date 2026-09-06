from fastapi import APIRouter
from Backend.app.schema.user_schema import UserCreateSchema
from Backend.app.service.user_service import UserService
from fastapi import Depends
from Backend.app.dependency.service_dependency import get_user_service

user_router=APIRouter(
    prefix="/",
    tags=""
)
@user_router.post("/")
def create_user(user_schema:UserCreateSchema,user_service:UserService=Depends(get_user_service)):
    user=user_service.create_user(user_schema)
    return user