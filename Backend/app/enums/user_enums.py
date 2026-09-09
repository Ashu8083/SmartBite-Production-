from enum import Enum

class UserStatus(str,Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"

class Gender(str,Enum):
    MALE="MALE"
    FEMALE="FEMALE"
    OTHER="OTHER"