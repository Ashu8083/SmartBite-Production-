from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.exception.app_exception import AppException

async def app_exception_handler(request:Request,exc:AppException):
    return JSONResponse(status_code=exc.status_code,
                        content={
                            "success":False,
                            "error":{
                                "code":exc.error_code,
                                "message":exc.message
                            }

                        }
    )

async def validation_exception_handler(request:Request,exc:RequestValidationError):
    return JSONResponse(status_code=422,
                        content={
                            "success":False,
                            "error":{
                                "code":"VALIDATION_ERROR",
                                "message":"validation error."
                            }
                        }
    )  

async def generic_exception_handler(request:Request,exc:Exception):
    return JSONResponse(status_code=500,
                        content={
                            "success":False,
                            "error":{
                                "code":"INTERNAL_SERVER_ERROR",
                                "message":"internal server error"
                            }
                        }

    )          
    