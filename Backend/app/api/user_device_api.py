from fastapi import APIRouter,Depends
from app.schema.userDevice_schema import UserDeviceCreate
from app.service.user_device_service import UserDeviceService
from app.dependency.service_dependency import get_user_device_service
from uuid import UUID
user_device_router=APIRouter(
    prefix="/userdevice",
    tags=["UserDevice"]
)

@user_device_router.post("")
def create_user_device(user_device_schema:UserDeviceCreate,user_device_service:UserDeviceService=Depends(get_user_device_service)):
    user_device=user_device_service.create_user_device(user_device_schema)
    return user_device

@user_device_router.get("/get-user-device-by-id")
def get_user_device_by_id(id:UUID,user_device_service:UserDeviceService=Depends(get_user_device_service)):
    user_device=user_device_service.get_user_device_by_id(id)
    return user_device


