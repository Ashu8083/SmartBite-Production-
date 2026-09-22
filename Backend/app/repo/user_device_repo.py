from sqlalchemy.orm import Session
from app.model.user_device_model import UserDevice
from uuid import UUID

class UserDeviceRepo:
    def __init__(self,db:Session):
        self.db=db

    def create_user_device(self,user_device:UserDevice):
        self.db.add(user_device)
        self.db.commit()
        self.db.refresh(user_device)
        return user_device 
    
    def get_user_device_by_id(self,id:UUID):
        user_device=self.db.query(UserDevice).filter(UserDevice.id==id).first()
        return user_device
    
    def get_all_user_device(self):
        user_device=self.db.query(UserDevice).filter().all()
        return user_device

    def get_user_device_by_user_id(self,user_id:UUID):
        user_device=self.db.query(UserDevice).filter(UserDevice.id==user_id).first()
        return user_device 
    
    def get_user_device_by_device_id(self,device_id:UUID):
        user_device=self.db.query(UserDevice).filter(UserDevice.device_id==device_id).first()
        return user_device
    
    def get_user_device_by_device_type(self,device_type:str):
        user_device=self.db.query(UserDevice).filter(UserDevice.device_type==device_type).first()
        return user_device

    def delete_user_device(self,device_id:UUID):
        device=self.db.query(UserDevice).filter(UserDevice.id==device_id).first()
        if not device:
            return None
        self.db.delete(device)
        self.db.commit()
        return device