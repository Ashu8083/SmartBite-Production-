from uuid import UUID
from datetime import datetime
from fastapi import HTTPException

from app.repo.user_device_repo import UserDeviceRepo
from app.schema.userDevice_schema import UserDeviceCreate
from app.model.user_device_model import UserDevice


class UserDeviceService:
    def __init__(self,user_device_repository:UserDeviceRepo):
        self.user_device_repo:UserDeviceRepo=user_device_repository

    def create_user_device(self,user_device_schema:UserDeviceCreate):
        try:
            user_device = UserDevice(
                user_id = user_device_schema.user_id,
                device_id = user_device_schema.device_id,
                device_type = user_device_schema.device_type,
                firebase_fcm_token = user_device_schema.firebase_fcm_token,
                last_login=datetime.utcnow()
            )
            return self.user_device_repo.create_user_device(user_device)
        except Exception as e:
            raise HTTPException(
            status_code=500,
            detail=f"Failed to create user device: {str(e)}"
        )
    
    def get_user_device_by_id(self,id:UUID):
        user_device=self.user_device_repo.get_user_device_by_id(id)
        if not user_device:
            raise HTTPException(
                status_code=404,
                detail="This id is not found."
            )
        return user_device

    def get_all_user_device(self):
        return self.user_device_repo.get_all_user_device()

    def get_user_device_by_user_id(self,user_id:UUID):
        user_device=self.user_device_repo.get_user_device_by_user_id(user_id)
        if user_device is None:
            raise HTTPException(
                status_code=404,
                detail="This user_id is not valid."
            )
        return user_device

    def get_user_device_by_device_id(self,device_id:UUID):
        user_device=self.user_device_repo.get_user_device_by_device_id(device_id)
        if user_device is None:
            raise HTTPException(
                status_code=404,
                detail="This device_id is invalid."
            )

    def get_user_device_by_device_type(self,device_type:str):
        return self.user_device_repo.get_user_device_by_device_type(device_type)


    def delete_user_device(self,device_id:UUID):
        user_device=self.user_device_repo.delete_user_device(device_id)
        if user_device is None:
            raise HTTPException(
                status_code = 404,
                detail="User device not found."
            )
        return {
            "message":"User device deleted successfully."
        }
