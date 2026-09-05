from enum import Enum

class UserStatus(Enum,str):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"

class Gender(Enum,str):
    MALE="MALE"
    FEMALE="FEMALE"
    OTHER="OTHER"