from pydantic import BaseModel
from uuid import UUID


class UserDeviceCreate(BaseModel):
    user_id:UUID
    device_id:UUID
    device_type:str
    firebase_fcm_token:str | None = None
    
