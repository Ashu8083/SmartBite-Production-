from fastapi import FastAPI
from fastapi import Request, Response,APIRouter


app = FastAPI()


@app.get("/hello")
def read_hello():
    return {"message": "SmartBite!"}
