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

@user_device_router.get("/get-all-user-device")
def get_all_user_device(user_device_service:UserDeviceService=Depends(get_user_device_service)):
    user_device=user_device_service.get_all_user_device()
    return user_device

@user_device_router.get("/get-user-device-by-user-id")
def get_user_device_by_user_id(user_id:UUID,user_device_service:UserDeviceService=Depends(get_user_device_service)):
    user_device=user_device_service.get_user_device_by_user_id(user_id)
    return user_device

@user_device_router.get("/get-user-device-by-device-id")
def get_user_device_by_device_id(device_id:UUID,user_device_service:UserDeviceService=Depends(get_user_device_service)):
    user_device=user_device_service.get_user_device_by_device_id(device_id)
    return user_device

@user_device_router.get("/get-user-device-by-device-type")
def get_user_device_by_device_type(device_type:str,user_device_service:UserDeviceService=Depends(get_user_device_service)):
    user_device=user_device_service.get_user_device_by_device_type(device_type)
    return user_device


