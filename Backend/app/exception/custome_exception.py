from app.exception.app_exception import AppException

class UserAlreadyExist(AppException):
    def __init__(self,message:str):
        super().__init__(message=message,status_code=409,error_code="USER_CONFLICT")

class UserNotFoundException(AppException):
    def __init__(self, message:str):
        super().__init__(message=message, status_code=404, error_code="USER_NOT_FOUND")

class EmailAlreadyExist(AppException):
    def __init__(self,message:str):
        super().__init__(message=message,status_code=409,error_code="EMAIL_CONFLICT")

class EmailNotFoundException(AppException):
    def __init__(self,message:str):
        super().__init__(message=message,status_code=404,error_code="Email_NOT_FOUND")

class UserDeviceAlreadyExist(AppException):
    def __init__(self,message:str):
        super().__init__(message=message,status_code=409,error_code="USER_DEVICE_EXIST")